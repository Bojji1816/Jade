from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "trackers" / "concept-renders" / "CAD"
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"


ITEMS = [
    {
        "id": "M001",
        "title": "青霧小手牌透光吊墜",
        "subtitle": "open-back / floating support 吊墜",
        "size": "23.9 x 12.8 x 4.9mm",
        "shape": "bar",
        "metal": "silver",
        "front": ["開窗背托離開皮膚", "上方小吊圈接幼銀鏈", "兩點承托保留入光"],
        "side": ["玉件離皮膚少許", "背後留光窗"],
        "notes": [
            "不做手鏈，改短項鏈吊墜。",
            "重點係背後留光，避免貼皮膚後失去透光雪花感。",
            "托位要包住上下受力點，吊圈焊在金屬托，不直接拉玉件。",
        ],
    },
    {
        "id": "M002",
        "title": "淡湖無事牌項鏈",
        "subtitle": "保留銀扣，銀鏈 / 皮繩 / 蠟繩可替換",
        "size": "32.9 x 12.4 x 4.8mm",
        "shape": "long_pendant",
        "metal": "silver",
        "front": ["原有銀扣 / 瓜子扣", "細長無事牌垂直重心", "可換 3 種鏈材"],
        "side": ["扣頭要可自由擺動", "鏈不可磨玉頂"],
        "notes": [
            "檢查原有銀扣焊位及磨損，質感不足就換 925 銀扣。",
            "三種鏈只改 tone，不改玉件結構。",
            "拍攝時同角度比較銀鏈、皮繩、蠟繩。",
        ],
    },
    {
        "id": "M003",
        "title": "煙墨厚身甜甜圈吊墜",
        "subtitle": "黑繩穿中孔，中性厚身吊墜",
        "size": "17.0 x 7.7 x 6.8mm",
        "shape": "donut_pendant",
        "metal": "dark",
        "front": ["黑繩穿過中孔", "保留厚身甜甜圈輪廓", "繩結藏在背後 / 側後"],
        "side": ["厚身 6.8mm 要展示", "孔口要拋滑"],
        "notes": [
            "不做牌仔，不加多餘金屬框。",
            "用黑皮繩或黑蠟繩放大煙墨中性 tone。",
            "確認繩徑可以順暢穿過中孔，避免磨孔。",
        ],
    },
    {
        "id": "M005",
        "title": "淡藍青幾何小吊墜",
        "subtitle": "短銀針 + 貼石小銀珠 + 幼銀鏈",
        "size": "18.7 x 7.7 x 4.2mm",
        "shape": "side_pin",
        "metal": "silver",
        "front": ["側肩橫孔穿短銀針", "兩端小銀珠貼住石頭", "兩側接小圈再連幼銀鏈"],
        "side": ["銀針外露要短", "銀珠貼石但不迫裂"],
        "notes": [
            "孔位在上方側肩橫穿，不是正頂中央。",
            "銀針短一點，兩粒小銀珠剛好貼住石頭。",
            "檢查孔口有無利邊，必要時先輕拋孔。",
        ],
    },
    {
        "id": "M006",
        "title": "晴青拱頂梯形吊墜",
        "subtitle": "正頂中央相連雙孔，銀鏈 / 蠟繩穿線",
        "size": "15.3 x 10.0 x 7.3mm",
        "shape": "top_connected_holes",
        "metal": "silver",
        "front": ["兩孔位於正上方", "孔道相連：一入一出", "可穿銀鏈或黑蠟繩"],
        "side": ["孔位不是兩角", "厚身 7.3mm 注意線徑"],
        "notes": [
            "兩個洞是正頂中央互通孔，不是左右角位吊點。",
            "銀鏈版較精緻；黑蠟繩版較 casual / 中性。",
            "確認孔口順滑，避免鏈或蠟繩長期磨損。",
        ],
    },
    {
        "id": "M007",
        "title": "灰月甜甜圈耳線",
        "subtitle": "短銀針固定珠組，單耳半長耳線",
        "size": "14.2 x 2.5mm",
        "shape": "threader",
        "metal": "silver",
        "front": ["耳線縮短至半長", "細銀珠 + 扁小玉珠 + 細銀珠", "下方甜甜圈自然垂下"],
        "side": ["短銀針固定珠組", "每邊只戴一隻"],
        "notes": [
            "首選短銀針固定珠組，避免玉珠滑動。",
            "耳線不需要吊太長，約原先一半長度較適合。",
            "左右長度和小圈焊位要對稱，戴上耳不應偏重。",
        ],
    },
    {
        "id": "M008",
        "title": "糯冰小平安扣耳環",
        "subtitle": "小 huggie + 小銀圈穿中孔",
        "size": "15.1 x 3.7 x 3.4mm",
        "shape": "huggie_donut",
        "metal": "silver",
        "front": ["小 huggie 作耳扣", "小銀圈穿過中孔", "平安扣自然垂下"],
        "side": ["左右垂墜高度一致", "中孔邊位要滑"],
        "notes": [
            "以小銀圈穿中孔，不需要包邊。",
            "左右兩粒厚薄、大小、垂墜高度要先配對。",
            "小圈直徑要夠活動，但不可令吊墜太低。",
        ],
    },
    {
        "id": "M009",
        "title": "糯冰飄綠牌仔耳環",
        "subtitle": "銀色耳勾，中孔簡潔接件",
        "size": "約18.5 x 13.9 x 2.9mm",
        "shape": "slot_earring",
        "metal": "silver",
        "front": ["銀色耳勾", "小圈 / 短接件穿中間長孔", "不加兩側銀線和底珠"],
        "side": ["玉牌保持垂直", "中孔受力位要拋滑"],
        "notes": [
            "保留中間長孔作唯一接駁點。",
            "不要底部小銀珠，也不要兩側銀線。",
            "重點是糯冰底和飄綠色帶，五金要乾淨簡短。",
        ],
    },
    {
        "id": "M010",
        "title": "糯冰深飄綠牌仔耳環",
        "subtitle": "金色耳勾，中孔簡潔接件",
        "size": "15.0 x 10.9 x 3.0mm",
        "shape": "slot_earring",
        "metal": "gold",
        "front": ["金色耳勾", "小圈 / 短接件穿中間長孔", "不加兩側金線和底珠"],
        "side": ["玉牌保持垂直", "金色襯深綠花"],
        "notes": [
            "用番已確認金色首選款。",
            "不加底部金珠，不加兩側金線，避免搶走深綠飄花。",
            "檢查左右花色及耳勾高度是否平衡。",
        ],
    },
    {
        "id": "M011",
        "title": "糯冰灰黑牌仔耳環",
        "subtitle": "槍黑 huggie / 氧化銀耳勾，中性冷調",
        "size": "12.8 x 9.1 x 3.0mm",
        "shape": "dark_slot_earring",
        "metal": "gunmetal",
        "front": ["槍黑 huggie 或氧化銀耳勾", "短接件穿中孔", "呼應烏雞灰黑紋理"],
        "side": ["短耳墜比例", "五金不宜太亮"],
        "notes": [
            "烏雞灰黑紋理適合黑銀 / 氧化銀 / 槍黑色。",
            "風格要偏中性，不要太甜美。",
            "若用電鍍或氧化色，需留意長期磨損露色。",
        ],
    },
    {
        "id": "M012",
        "title": "糯冰灰白黑紋幾何吊墜",
        "subtitle": "true bezel 全包邊壓邊小吊墜",
        "size": "14.0 x 10.9 x 2.3mm",
        "shape": "bezel_pendant",
        "metal": "black",
        "front": ["金屬 lip 微覆蓋玉面邊緣", "吊圈焊在金屬框上", "銀色或黑色包邊"],
        "side": ["薄身 2.3mm 要底托", "不可只做外框"],
        "notes": [
            "M012 和 M004 一樣，不能只靠外框視覺，必須有壓邊 lip。",
            "背面建議薄底托或 open-back 底托保護薄身邊角。",
            "黑色包邊要評估氧化 / 電鍍磨損露色。",
        ],
    },
]


def font(size, bold=False):
    return ImageFont.truetype(FONT_PATH, size=size)


def text(draw, xy, value, size=28, fill="#25312d", bold=False):
    draw.text(xy, value, font=font(size, bold), fill=fill)


def line_arrow(draw, start, end, fill="#50615a", width=5):
    draw.line([start, end], fill=fill, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    length = 24
    a1 = angle + math.pi * 0.84
    a2 = angle - math.pi * 0.84
    p1 = (end[0] + length * math.cos(a1), end[1] + length * math.sin(a1))
    p2 = (end[0] + length * math.cos(a2), end[1] + length * math.sin(a2))
    draw.polygon([end, p1, p2], fill=fill)


def rounded_panel(draw, box):
    draw.rounded_rectangle(box, radius=14, fill="#ffffff", outline="#cfd6d0", width=3)


def metal_color(kind):
    return {
        "silver": "#d9dddc",
        "gold": "#d9b55d",
        "dark": "#353a3a",
        "gunmetal": "#404345",
        "black": "#25282a",
    }.get(kind, "#d9dddc")


def draw_jade_shape(draw, item, cx, cy, scale=1.0):
    shape = item["shape"]
    jade = "#d7ebe5"
    edge = "#879b96"
    vein = "#6f8d85"
    if shape == "bar":
        draw.rounded_rectangle([cx - 70, cy - 145, cx + 70, cy + 145], radius=24, fill=jade, outline=edge, width=5)
        draw.line([(cx - 32, cy - 115), (cx + 22, cy + 118)], fill=vein, width=4)
    elif shape == "long_pendant":
        draw.rounded_rectangle([cx - 55, cy - 160, cx + 55, cy + 160], radius=18, fill=jade, outline=edge, width=5)
        draw.line([(cx - 20, cy - 110), (cx + 30, cy + 95)], fill=vein, width=4)
    elif shape in {"donut_pendant", "huggie_donut", "threader"}:
        draw.ellipse([cx - 105, cy - 105, cx + 105, cy + 105], fill=jade, outline=edge, width=5)
        draw.ellipse([cx - 43, cy - 43, cx + 43, cy + 43], fill="#ffffff", outline=edge, width=4)
        draw.arc([cx - 85, cy - 85, cx + 85, cy + 85], 215, 330, fill="#eef7f4", width=8)
    elif shape == "side_pin":
        pts = [(cx - 52, cy - 135), (cx + 58, cy - 105), (cx + 42, cy + 145), (cx - 62, cy + 120)]
        draw.polygon(pts, fill=jade, outline=edge)
        draw.line(pts + [pts[0]], fill=edge, width=5)
    elif shape == "top_connected_holes":
        pts = [(cx - 72, cy - 95), (cx - 28, cy - 140), (cx + 45, cy - 135), (cx + 72, cy - 92), (cx + 58, cy + 135), (cx - 62, cy + 135)]
        draw.polygon(pts, fill=jade, outline=edge)
        draw.line(pts + [pts[0]], fill=edge, width=5)
    elif shape in {"slot_earring", "dark_slot_earring"}:
        draw.rounded_rectangle([cx - 80, cy - 110, cx + 80, cy + 110], radius=22, fill=jade, outline=edge, width=5)
        draw.rounded_rectangle([cx - 12, cy - 62, cx + 12, cy + 42], radius=9, fill="#f7f8f5", outline=edge, width=3)
        if shape == "dark_slot_earring":
            draw.line([(cx - 52, cy - 70), (cx + 42, cy + 80)], fill="#4e5a57", width=7)
    elif shape == "bezel_pendant":
        m = metal_color(item["metal"])
        pts = [(cx - 85, cy - 110), (cx + 72, cy - 95), (cx + 90, cy + 95), (cx - 52, cy + 125), (cx - 92, cy + 45)]
        draw.polygon(pts, fill=m)
        inner = [(cx - 68, cy - 88), (cx + 56, cy - 77), (cx + 69, cy + 76), (cx - 43, cy + 98), (cx - 70, cy + 34)]
        draw.polygon(inner, fill=jade)
        draw.line(pts + [pts[0]], fill="#101214", width=4)
        draw.line(inner + [inner[0]], fill="#879b96", width=3)
        return
    else:
        draw.ellipse([cx - 80, cy - 100, cx + 80, cy + 100], fill=jade, outline=edge, width=5)


def draw_hardware(draw, item, cx, cy):
    m = metal_color(item["metal"])
    shape = item["shape"]
    if shape == "bar":
        draw.arc([cx - 110, cy - 180, cx + 110, cy - 60], 200, 340, fill=m, width=8)
        draw.rectangle([cx - 45, cy - 136, cx + 45, cy + 120], outline=m, width=8)
        draw.rectangle([cx - 22, cy - 105, cx + 22, cy + 92], outline="#f7f8f5", width=7)
    elif shape == "long_pendant":
        draw.ellipse([cx - 22, cy - 198, cx + 22, cy - 154], outline=m, width=8)
        draw.arc([cx - 170, cy - 290, cx + 170, cy - 150], 200, 340, fill=m, width=5)
    elif shape == "donut_pendant":
        draw.arc([cx - 140, cy - 165, cx + 140, cy + 75], 205, 335, fill=m, width=12)
    elif shape == "side_pin":
        draw.line([(cx - 92, cy - 112), (cx + 95, cy - 94)], fill=m, width=7)
        draw.ellipse([cx - 111, cy - 132, cx - 76, cy - 97], fill=m)
        draw.ellipse([cx + 76, cy - 114, cx + 111, cy - 79], fill=m)
        draw.line([(cx - 105, cy - 115), (cx - 185, cy - 210)], fill=m, width=5)
        draw.line([(cx + 100, cy - 96), (cx + 195, cy - 196)], fill=m, width=5)
    elif shape == "top_connected_holes":
        draw.ellipse([cx - 34, cy - 130, cx - 4, cy - 100], fill="#f7f8f5", outline="#879b96", width=3)
        draw.ellipse([cx + 7, cy - 130, cx + 37, cy - 100], fill="#f7f8f5", outline="#879b96", width=3)
        draw.arc([cx - 120, cy - 215, cx + 120, cy - 75], 205, 335, fill=m, width=8)
    elif shape == "threader":
        draw.line([(cx, cy - 250), (cx, cy - 145)], fill=m, width=6)
        draw.ellipse([cx - 17, cy - 160, cx + 17, cy - 126], fill=m)
        draw.rounded_rectangle([cx - 33, cy - 137, cx + 33, cy - 96], radius=12, fill="#d7ebe5", outline="#879b96", width=3)
        draw.ellipse([cx - 17, cy - 105, cx + 17, cy - 71], fill=m)
        draw.line([(cx, cy - 72), (cx, cy - 105)], fill=m, width=5)
    elif shape == "huggie_donut":
        draw.arc([cx - 75, cy - 215, cx + 75, cy - 65], 35, 320, fill=m, width=12)
        draw.ellipse([cx - 22, cy - 80, cx + 22, cy - 36], outline=m, width=7)
        draw.line([(cx, cy - 36), (cx, cy - 105)], fill=m, width=5)
    elif shape in {"slot_earring", "dark_slot_earring"}:
        draw.arc([cx - 78, cy - 285, cx + 78, cy - 128], 25, 330, fill=m, width=9)
        draw.ellipse([cx - 22, cy - 126, cx + 22, cy - 82], outline=m, width=7)
        draw.line([(cx, cy - 82), (cx, cy - 45)], fill=m, width=6)
    elif shape == "bezel_pendant":
        draw.ellipse([cx - 24, cy - 158, cx + 24, cy - 110], outline=m, width=8)
        draw.arc([cx - 150, cy - 260, cx + 150, cy - 125], 205, 335, fill=m, width=5)


def draw_side_section(draw, item, x, y):
    m = metal_color(item["metal"])
    draw.rounded_rectangle([x, y, x + 540, y + 230], radius=14, fill="#ffffff", outline="#cfd6d0", width=3)
    text(draw, (x + 34, y + 28), "側面 / 孔位", 32)
    draw.rounded_rectangle([x + 130, y + 110, x + 310, y + 152], radius=20, fill="#d7ebe5", outline="#879b96", width=4)
    draw.line([(x + 112, y + 160), (x + 330, y + 160)], fill=m, width=8)
    if item["shape"] in {"bar", "bezel_pendant"}:
        draw.rectangle([x + 118, y + 95, x + 322, y + 168], outline=m, width=6)
    if item["shape"] in {"side_pin", "top_connected_holes", "slot_earring", "dark_slot_earring"}:
        draw.ellipse([x + 185, y + 118, x + 214, y + 147], fill="#f7f8f5", outline="#879b96", width=3)
        draw.ellipse([x + 230, y + 118, x + 259, y + 147], fill="#f7f8f5", outline="#879b96", width=3)
    line_arrow(draw, (x + 360, y + 145), (x + 460, y + 145))
    text(draw, (x + 365, y + 170), item["side"][0], 23)
    if len(item["side"]) > 1:
        text(draw, (x + 365, y + 198), item["side"][1], 20, "#5b6661")


def draw_item(item):
    img = Image.new("RGB", (1600, 1600), "#f7f8f5")
    draw = ImageDraw.Draw(img)
    text(draw, (80, 58), f'{item["id"]} CAD-style 加工圖', 54)
    text(draw, (80, 125), item["title"], 30, "#4e5b56")
    text(draw, (80, 165), f'{item["subtitle"]}｜尺寸：{item["size"]}', 28, "#5b6661")

    rounded_panel(draw, [70, 240, 920, 990])
    text(draw, (115, 285), "正面 Front View", 36)
    cx, cy = 470, 610
    draw_hardware(draw, item, cx, cy)
    draw_jade_shape(draw, item, cx, cy)

    callouts = item["front"]
    targets = [(cx - 70, cy - 130), (cx + 65, cy - 35), (cx, cy + 110)]
    starts = [(135, 390), (675, 420), (680, 785)]
    for label, start, target in zip(callouts, starts, targets):
        line_arrow(draw, start, target)
        text(draw, (start[0] - 5, start[1] - 50), label, 25)

    text(draw, (120, 910), f'尺寸參考：{item["size"]}', 24, "#5b6661")

    draw_side_section(draw, item, 980, 240)

    rounded_panel(draw, [980, 520, 1530, 990])
    text(draw, (1015, 568), "加工備註", 34)
    y = 625
    for idx, note in enumerate(item["notes"], 1):
        text(draw, (1015, y), f"{idx}. {note}", 22)
        y += 76

    rounded_panel(draw, [70, 1055, 1530, 1265])
    text(draw, (105, 1102), "給工場確認", 32)
    checklist = "確認孔位/扣位 - 確認五金材質及顏色 - 確認重心及垂墜高度 - 確認磨孔/刮手風險 - 製作前回圖確認"
    text(draw, (105, 1160), checklist, 25)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f'{item["id"]}-cad-plan.png'
    img.save(out, "PNG", optimize=True)
    return out


def main():
    for item in ITEMS:
        out = draw_item(item)
        print(out)


if __name__ == "__main__":
    main()
