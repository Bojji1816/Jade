import csv
import html
import subprocess
from io import StringIO
from pathlib import Path

from PIL import Image as PILImage
from PIL import ImageOps
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "trackers" / "material-inventory.md"
OUT_DIR = ROOT / "output" / "pdf"
TMP_DIR = ROOT / "tmp" / "pdfs" / "stock-inventory-assets"
PDF_PATH = OUT_DIR / "jade-stock-inventory-list.pdf"
PDF_FONT_PATH = Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf")
FONT_NAME = "ArialUnicode"


FIELDS = [
    "編號",
    "入貨日期",
    "貨品",
    "數量",
    "成本",
    "尺寸",
    "入貨地點/檔口",
    "顏色/種水觀察",
    "裂/棉/瑕疵",
    "形狀/用途",
    "照片位置",
    "尺寸圖",
    "狀態",
    "備註",
]


def split_markdown_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def read_inventory():
    rows = []
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| M"):
            continue
        cells = split_markdown_row(line)
        rows.append(dict(zip(FIELDS, cells)))
    return rows


def register_font():
    global FONT_NAME
    if PDF_FONT_PATH.exists():
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(PDF_FONT_PATH)))
    else:
        FONT_NAME = "STSong-Light"
        pdfmetrics.registerFont(UnicodeCIDFont(FONT_NAME))


def split_paths(value):
    if not value or value == "待補":
        return []
    return [p.strip().strip("`") for p in value.split(";") if p.strip()]


def resolve_image(path_text):
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path if path.exists() else None


def prepared_image(path):
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.lower()
    out = TMP_DIR / (f"{path.name}.png" if suffix in {".heic", ".heif"} else f"{path.stem}.jpg")
    if suffix not in {".heic", ".heif"} and out.exists() and out.stat().st_mtime >= path.stat().st_mtime:
        return out

    if suffix in {".heic", ".heif"}:
        if out.exists() and out.stat().st_mtime >= path.stat().st_mtime:
            return out
        subprocess.run(["qlmanage", "-t", "-s", "1200", "-o", str(TMP_DIR), str(path)], check=True)
        generated = TMP_DIR / f"{path.name}.png"
        if generated != out:
            generated.replace(out)
        return out

    with PILImage.open(path) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        im.thumbnail((1500, 1500), PILImage.Resampling.LANCZOS)
        im.save(out, "JPEG", quality=86, optimize=True, progressive=True)
    return out


def image_flowable(path, max_w, max_h):
    image_path = prepared_image(path)
    with PILImage.open(image_path) as im:
        w, h = im.size
    scale = min(max_w / w, max_h / h)
    return Image(str(image_path), width=w * scale, height=h * scale)


def esc(text):
    return html.escape(str(text)).replace("\n", "<br/>")


def p(text, style):
    return Paragraph(esc(text), style)


def table(data, col_widths, style, header=False):
    wrapped = [[p(cell, style) for cell in row] for row in data]
    t = Table(wrapped, colWidths=col_widths, hAlign="LEFT", repeatRows=1 if header else 0)
    rules = [
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#d8ded8")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if header:
        rules.extend([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e5ece6")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1f2b26")),
        ])
    t.setStyle(TableStyle(rules))
    return t


def pick_images(item):
    photo_paths = [resolve_image(p) for p in split_paths(item["照片位置"])]
    size_paths = [resolve_image(p) for p in split_paths(item["尺寸圖"])]
    paths = [p for p in photo_paths + size_paths if p]
    finished = [p for p in paths if "/finished/" in str(p)]
    main = finished[0] if finished else (paths[0] if paths else None)
    supporting = [p for p in paths if p != main]
    return main, supporting[:4], paths


def image_grid(paths, small):
    if not paths:
        return p("未有補充圖片", small)

    cells = []
    row = []
    for idx, path in enumerate(paths):
        block = [
            image_flowable(path, 37 * mm, 32 * mm),
            Spacer(1, 1.2 * mm),
            p(path.name, small),
        ]
        row.append(block)
        if len(row) == 4:
            cells.append(row)
            row = []
    if row:
        while len(row) < 4:
            row.append("")
        cells.append(row)

    t = Table(cells, colWidths=[39 * mm] * 4, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def item_card(item, styles):
    base, small, h2, label = styles
    main, supporting, all_paths = pick_images(item)
    info = [
        ["入貨日期", item["入貨日期"], "數量", item["數量"]],
        ["成本", item["成本"], "尺寸", item["尺寸"]],
        ["來源", item["入貨地點/檔口"], "狀態", item["狀態"]],
        ["用途", item["形狀/用途"], "瑕疵/QC", item["裂/棉/瑕疵"]],
        ["顏色/種水", item["顏色/種水觀察"], "備註", item["備註"]],
    ]
    info_table = table(info, [17 * mm, 47 * mm, 18 * mm, 54 * mm], small)
    main_block = [p("主圖", label)]
    if main:
        main_block.append(image_flowable(main, 42 * mm, 48 * mm))
        main_block.append(Spacer(1, 1.5 * mm))
        main_block.append(p(main.name, small))
    else:
        main_block.append(p("未有圖片", small))

    content = [
        p(f'{item["編號"]} - {item["貨品"]}', h2),
        Table(
            [[main_block, info_table]],
            colWidths=[46 * mm, 138 * mm],
            hAlign="LEFT",
            style=[
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ],
        ),
        p("尺寸/補充圖", label),
        image_grid(supporting, small),
        p("圖片路徑：" + ("; ".join(str(p.relative_to(ROOT)) for p in all_paths) if all_paths else "待補"), small),
    ]
    return KeepTogether(content)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONT_NAME, 8)
    canvas.setFillColor(colors.HexColor("#67716b"))
    canvas.drawString(12 * mm, 8 * mm, "Jade Stock Inventory List")
    canvas.drawRightString(198 * mm, 8 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    register_font()

    styles = getSampleStyleSheet()
    base = ParagraphStyle(
        "Base",
        parent=styles["Normal"],
        fontName=FONT_NAME,
        fontSize=8.6,
        leading=11.6,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#26302b"),
    )
    small = ParagraphStyle(
        "Small",
        parent=base,
        fontSize=7.1,
        leading=9.6,
        textColor=colors.HexColor("#59635d"),
    )
    title = ParagraphStyle(
        "Title",
        parent=base,
        fontSize=26,
        leading=34,
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    subtitle = ParagraphStyle(
        "Subtitle",
        parent=base,
        fontSize=11.2,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#52605a"),
    )
    h1 = ParagraphStyle(
        "H1",
        parent=base,
        fontSize=15,
        leading=20,
        spaceBefore=6,
        spaceAfter=6,
    )
    h2 = ParagraphStyle(
        "H2",
        parent=base,
        fontSize=12.2,
        leading=16,
        spaceBefore=6,
        spaceAfter=5,
        textColor=colors.HexColor("#1f2b26"),
    )
    label = ParagraphStyle(
        "Label",
        parent=base,
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#33433b"),
    )

    items = read_inventory()
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=A4,
        rightMargin=12 * mm,
        leftMargin=12 * mm,
        topMargin=12 * mm,
        bottomMargin=13 * mm,
        title="Jade Stock Inventory List",
    )

    story = [
        Spacer(1, 25 * mm),
        p("翡翠貨存清單", title),
        p("M001-M028 | 包含入貨資料、成本、尺寸、來源、狀態、備註及圖片", subtitle),
        Spacer(1, 8 * mm),
        p("更新日期：2026-08-13", subtitle),
        Spacer(1, 16 * mm),
        p(f"資料來源：{SOURCE.relative_to(ROOT)}", base),
        p(f"總件數：{len(items)} 個編號。M026-M028 為未取回毛料，待拋光後補尺寸和 QC。", base),
        PageBreak(),
        p("貨存總覽", h1),
    ]

    overview = [["編號", "貨品", "數量", "成本", "尺寸", "來源", "狀態"]]
    for item in items:
        overview.append([
            item["編號"],
            item["貨品"],
            item["數量"],
            item["成本"],
            item["尺寸"],
            item["入貨地點/檔口"],
            item["狀態"],
        ])
    story.append(table(overview, [14 * mm, 40 * mm, 14 * mm, 34 * mm, 32 * mm, 40 * mm, 22 * mm], small, header=True))
    story.append(PageBreak())
    story.append(p("逐件貨存資料", h1))

    style_tuple = (base, small, h2, label)
    for idx, item in enumerate(items):
        story.append(item_card(item, style_tuple))
        if idx != len(items) - 1:
            story.append(Spacer(1, 4 * mm))
            if idx % 2 == 1:
                story.append(PageBreak())

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(PDF_PATH)


if __name__ == "__main__":
    build_pdf()
