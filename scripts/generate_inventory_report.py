from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
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
OUT_DIR = ROOT / "output" / "pdf"
ASSET_DIR = OUT_DIR / "assets"
PDF_PATH = OUT_DIR / "jade-inventory-product-plan.pdf"
PHOTO_DIR = ROOT / "trackers" / "images"
RENDER_DIR = ROOT / "trackers" / "concept-renders"
CAD_DIR = RENDER_DIR / "CAD"

PDF_FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
PDF_FONT_NAME = "ArialUnicode"

CAD_DIAGRAMS = {
    "M001": ("CAD 加工圖：open-back / floating support 吊墜", CAD_DIR / "M001-cad-plan.png"),
    "M002": ("CAD 加工圖：銀扣及三種鏈款結構", CAD_DIR / "M002-cad-plan.png"),
    "M003": ("CAD 加工圖：厚身甜甜圈黑繩穿中孔", CAD_DIR / "M003-cad-plan.png"),
    "M004": ("CAD 加工圖：half bezel + visible micro prongs", RENDER_DIR / "M004" / "M004-cad-half-bezel-visible-prongs.png"),
    "M005": ("CAD 加工圖：短銀針 + 貼石小銀珠", CAD_DIR / "M005-cad-plan.png"),
    "M006": ("CAD 加工圖：正頂中央相連雙孔穿線", CAD_DIR / "M006-cad-plan.png"),
    "M007": ("CAD 加工圖：短銀針固定珠組半長耳線", CAD_DIR / "M007-cad-plan.png"),
    "M008": ("CAD 加工圖：小 huggie + 中孔小銀圈", CAD_DIR / "M008-cad-plan.png"),
    "M009": ("CAD 加工圖：銀色耳勾中孔簡潔接件", CAD_DIR / "M009-cad-plan.png"),
    "M010": ("CAD 加工圖：金色耳勾中孔簡潔接件", CAD_DIR / "M010-cad-plan.png"),
    "M011": ("CAD 加工圖：槍黑 / 氧化銀中性耳墜", CAD_DIR / "M011-cad-plan.png"),
    "M012": ("CAD 加工圖：true bezel 全包邊壓邊吊墜", CAD_DIR / "M012-cad-plan.png"),
}


ITEMS = [
    {
        "id": "M001",
        "name": "青霧小手牌透光吊墜",
        "category": "入門小吊墜 / 透光設計款",
        "photo": "M001-IMG_5819.JPG",
        "size": "23.9 x 12.8 x 4.9mm",
        "cost": "100（幣種待補）",
        "decision": "手牌太短，不適合做手鏈。吊墜方向成立，但要避免貼皮膚後失去透光雪花感；主推托起玉件、保留背後入光的吊墜設計。暫定 Style 02 或 Style 03。",
        "direction": "做短項鏈吊墜，採用 open-back / window-back / two-point floating support，令玉件離開皮膚少許，增加受光度。",
        "process": "檢查邊角及裂 - 確認最穩固承托點 - 做 925 銀開窗托或兩點浮托 - 試上頸透光 - QC。",
        "copy": "青灰綠底色帶雪花棉，像一小片被托起的霧光。吊墜背後留光，戴上身仍然看得到玉的通透層次。",
        "ig": "有些玉，要留一點光給它。這枚青霧小手牌用托起的方式做吊墜，讓雪花棉和透光感不會被皮膚吃掉。",
        "price": "HK$580-880",
        "shoot": "透光對比、側面托起結構、白衫上頸、手持比例。",
        "renders": [
            ("Style 02 主推：開窗背托", "M001/shortlist/M001-style-02-window-back-support.png"),
            ("Style 03 備選：兩點浮托", "M001/shortlist/M001-style-03-floating-two-point.png"),
        ],
        "worn": ("配戴預想：鎖骨鏈透光感", "M001/worn-01-necklace-window-support.png"),
    },
    {
        "id": "M002",
        "name": "淡湖無事牌項鏈",
        "category": "主力日常翡翠 / 送禮款",
        "photo": "M002-IMG_5829.JPG",
        "size": "32.9 x 12.4 x 4.8mm",
        "cost": "400 CNY",
        "decision": "本身已有銀扣，可直接測不同鏈帶來的氣質。銀鏈最精緻，皮繩較中性，蠟繩較 casual。",
        "direction": "保留原有銀扣，先以三種鏈測 tone：銀鏈、皮繩、蠟繩。",
        "process": "檢查扣頭及鏈 - 清潔拋光 - 準備三種鏈款 - 拍攝同一構圖比較 - 選主推鏈款。",
        "copy": "細長無事牌由淡青綠慢慢過渡到深綠飄花。換一條鏈，氣質就由精緻變得中性或輕鬆。",
        "ig": "一件無事牌，三種日常語氣。銀鏈乾淨，皮繩沉穩，蠟繩輕鬆，讓同一件玉走入不同穿搭。",
        "price": "HK$980-1380",
        "shoot": "白衫/黑衫上頸、扣頭近鏡、三種鏈同角度比較、禮盒照。",
        "renders": [
            ("銀鏈：精緻日常", "M002/chain-01-silver-chain.png"),
            ("皮繩：中性沉穩", "M002/chain-02-leather-cord.png"),
            ("蠟繩：輕鬆 casual", "M002/chain-03-waxed-cord.png"),
        ],
        "worn": ("配戴預想：銀鏈日常上頸", "M002/worn-01-silver-chain-necklace.png"),
    },
    {
        "id": "M003",
        "name": "煙墨厚身甜甜圈吊墜",
        "category": "中性/男裝測款",
        "photo": "M003-IMG_5826.JPG",
        "size": "17.0 x 7.7 x 6.8mm",
        "cost": "380 CNY",
        "decision": "M003 是煙墨厚身甜甜圈 / 平安扣吊墜，不是牌仔或細吊咀。重點要保留厚身圓潤感和中孔結構，以黑色繩款放大中性煙墨 tone。",
        "direction": "做中性厚身甜甜圈吊墜，以黑皮繩或黑蠟繩穿過中孔作主推；銀鏈只作後備精緻版本。",
        "process": "檢查中孔內壁及邊位 - 確認繩徑可順暢穿過中孔 - 保留厚身圓潤感 - 確認吊墜重心 - 拍側面厚度及男女配戴。",
        "copy": "灰白底色混入墨綠與黑花，比傳統綠翡翠更低調。厚身甜甜圈輪廓圓潤，戴起來有安靜的份量感。",
        "ig": "不是所有翡翠都要很綠。煙墨色甜甜圈更冷靜、更中性，適合想戴玉但不想太傳統的人。",
        "price": "HK$780-1080",
        "shoot": "男裝黑 Tee、手掌比例、側面厚度、中孔穿繩細節、煙墨花近鏡。",
        "renders": [
            ("主推：煙墨厚身甜甜圈黑繩吊墜", "M003/product-01-smoky-thick-donut-black-cord.png"),
        ],
        "worn": ("配戴預想：黑繩中性上頸", "M003/worn-01-smoky-donut-black-cord.png"),
    },
    {
        "id": "M004",
        "name": "淡青小如意戒指",
        "category": "戒面 / 迷你戒指測款",
        "photo": "M004-IMG_5832.JPG",
        "size": "9.3 x 6.8 x 2.8mm",
        "cost": "50 CNY",
        "decision": "太細、太薄，不適合做吊墜。戒面方向最能放大存在感；現階段 02 half bezel / side prong 最啱心水，作主推款。",
        "direction": "做 925 銀半包鑲側爪迷你戒指。保留玉面光感，同時避免 full bezel 太厚重。",
        "process": "確認厚度及孔位 - 設計半包邊與側爪 - 幼身銀戒臂 - 試戴重心 - 微距和上手拍攝。",
        "copy": "迷你如意形翡翠，淡白青色溫柔乾淨。用半包鑲托住，細粒也能被看見。",
        "ig": "這粒小如意太細，不適合硬做吊墜。做成半包鑲迷你戒面剛剛好，一點淡青白玉色，低調但有細節。",
        "price": "HK$680-980",
        "shoot": "微距、上手、側面戒臂、與素戒疊戴、戒面比例。",
        "renders": [
            ("01 full bezel：穩陣但較厚", "M004/ring-01-full-bezel.png"),
            ("02 修正版：half bezel + visible micro prongs", "M004/ring-05-half-bezel-visible-micro-prongs.png"),
            ("03 mini signet：存在感強", "M004/ring-03-mini-signet.png"),
            ("04 stacking ring：輕盈疊戴", "M004/ring-04-stacking-ring.png"),
        ],
        "worn": ("配戴預想：迷你戒面上手", "M004/worn-01-half-bezel-ring.png"),
    },
    {
        "id": "M005",
        "name": "淡藍青幾何小吊墜",
        "category": "入門小吊墜 / 幾何系列",
        "photo": "M005-IMG_5833.JPG",
        "size": "18.7 x 7.7 x 4.2mm",
        "cost": "100 CNY",
        "decision": "孔位在上方側肩位橫穿，不是正頂中央。主推短銀針穿過孔位，兩邊小銀珠剛好貼住石頭，再連接幼銀鏈；比單純穿鏈更完整、更像正式設計款。",
        "direction": "做短銀針小銀珠吊墜。銀針只作內部承托，外露部分極短，讓兩粒銀珠成為乾淨細節。",
        "process": "檢查側肩橫孔是否平滑 - 按孔徑配短銀針 - 兩端小銀珠貼石固定 - 連接幼銀鏈 - 確認重心及磨線風險 - 拍攝比例。",
        "copy": "淡藍青色的小幾何翡翠，線條自然不完全對稱。短銀針和兩粒小銀珠輕輕托住玉件，細節乾淨而完整。",
        "ig": "不是把鏈硬穿過去，而是用一支很短的銀針和兩粒小銀珠托住。淡藍青小幾何，多了一點設計感，但仍然很日常。",
        "price": "HK$580-780",
        "shoot": "頂部橫孔近鏡、白底平鋪、上頸、三種線材比較。",
        "renders": [
            ("主推：短銀針 + 貼石小銀珠", "M005/threading-06-short-pin-snug-silver-beads-chain.png"),
            ("側肩孔直接穿銀鏈", "M005/threading-04-corrected-side-shoulder-silver-chain.png"),
            ("初版銀針小銀珠", "M005/threading-05-silver-pin-beads-chain.png"),
        ],
        "worn": ("配戴預想：短銀針小銀珠上頸", "M005/worn-01-short-pin-silver-beads-necklace.png"),
    },
    {
        "id": "M006",
        "name": "晴青拱頂梯形吊墜",
        "category": "入門小吊墜 / 送禮小款",
        "photo": "M006-IMG_5834.JPG",
        "size": "15.3 x 10.0 x 7.3mm",
        "cost": "100 CNY",
        "decision": "頂部正中央有兩個相連孔位，可由一邊孔入、另一邊孔出。因孔位集中在拱頂中央，不適合做兩角吊點；主推銀鏈或黑蠟繩直接穿過中央短孔道。",
        "direction": "做厚身小吊墜，保留拱頂梯形輪廓，以正頂中央穿線展示玉件厚度和乾淨線條。",
        "process": "檢查正頂中央互通孔 - 測幼銀鏈及黑蠟繩線徑 - 確認孔口磨損及穿線順滑度 - 必要時輕拋孔口 - 拍側面厚度及正頂孔位。",
        "copy": "淡青綠色小吊墜，拱頂梯形輪廓帶一點建築感。厚身、圓潤，中央穿線後更簡潔。",
        "ig": "一枚小小的晴青梯形，厚身、圓潤、有份量。正上方中央穿線，少一件配件，多一點玉本身。",
        "price": "HK$580-780",
        "shoot": "側面厚度、正頂中央互通孔、透光、上頸短鏈、與 M005 對照。",
        "renders": [
            ("銀鏈：正頂中央互通孔", "M006/threading-07-centered-connected-top-holes-silver-chain.png"),
            ("黑蠟繩：正頂中央互通孔", "M006/threading-08-centered-connected-top-holes-black-waxed-cord.png"),
        ],
        "worn": ("配戴預想：正頂中央孔銀鏈上頸", "M006/worn-01-centered-top-hole-silver-chain.png"),
    },
    {
        "id": "M007",
        "name": "灰月甜甜圈耳線",
        "category": "快速上架 / 日常耳環",
        "photo": "M007-IMG_5835.JPG",
        "size": "14.2 x 2.5mm（單邊玉圈）",
        "cost": "80 CNY",
        "decision": "首選短銀針固定珠組耳線。用短銀針穿住「細銀珠 + 扁小玉珠 + 細銀珠」，兩端接回幼銀耳線和下方甜甜圈，令珠位固定而不失輕盈感。",
        "direction": "保留長銀耳線和灰月甜甜圈主體；上方珠組改為短銀針固定結構，兩粒細銀珠貼住扁小玉珠，比例更細緻。",
        "process": "確認耳線材質是否 925 銀 - 按珠孔配短銀針 - 穿細銀珠、扁小玉珠、細銀珠 - 兩端做小圈或焊接接鏈 - 檢查左右長度、孔位磨損和珠組穩固度 - 清潔及上耳拍攝。",
        "copy": "淡灰白青色甜甜圈耳線，長線條輕盈垂墜。上方一組扁小玉珠和細銀珠像一個固定的光點，令耳環更完整、更精緻。",
        "ig": "灰月色甜甜圈耳線，輕、淡、好配襯。這版加了短銀針固定珠組，小玉珠不再滑動，細節更乾淨，也更像正式設計款。",
        "price": "HK$780-980",
        "shoot": "上耳照、珠組近鏡、側面動態、長度比例、白衫和黑衫兩套。",
        "renders": [
            ("首選：短銀針固定珠組耳線", "M007/M007-threader-short-pin-fixed-bead-module.png"),
            ("備選：扁小玉珠 + 細銀珠耳線", "M007/M007-threader-flat-jade-bead-small-silver-spacers.png"),
        ],
        "worn": ("配戴預想：單耳半長耳線", "M007/worn-02-threader-half-length-single-ear.png"),
    },
    {
        "id": "M008",
        "name": "糯冰小平安扣耳環",
        "category": "第二批 / 快速耳飾款",
        "photo": "M008-IMG_5881.JPG",
        "size": "15.1 x 3.7 x 3.4mm",
        "cost": "5件總價945 CNY，單件未分配",
        "decision": "近白糯冰甜甜圈一對，已成對且形狀完整。比做單吊墜更適合做小耳環，可最快測試淡色糯冰耳飾接受度。",
        "direction": "做 925 銀小 huggie / 小圈耳環，平安扣以小銀圈穿過中孔自然垂下，走清爽日常款。",
        "process": "確認兩粒大小及厚薄是否一致 - 檢查中孔邊位 - 配小銀圈及 huggie - 確認左右垂墜高度 - 上耳拍攝。",
        "copy": "近白糯冰小平安扣，顏色乾淨柔和。配銀色小耳圈，像一對輕輕透光的日常耳飾。",
        "ig": "不是很搶眼的一對耳環，但很容易每天戴。近白糯冰平安扣配小銀圈，乾淨、輕、淡淡有光。",
        "price": "HK$580-780",
        "shoot": "白底商品照、上耳比例、側面垂墜、與 M007 灰月耳線對比。",
        "renders": [
            ("主推：糯冰平安扣 huggie 耳環", "M008/product-01-icy-donut-huggie-earrings.png"),
        ],
        "worn": ("配戴預想：小平安扣 huggie 上耳", "M008/worn-01-icy-donut-huggie.png"),
    },
    {
        "id": "M009",
        "name": "糯冰飄綠牌仔耳環",
        "category": "第二批 / 飄綠耳飾系列",
        "photo": "M009-IMG_5885.JPG",
        "size": "約18.5 x 13.9 x 2.9mm",
        "cost": "5件總價945 CNY，單件未分配",
        "decision": "首選銀色中孔簡潔耳勾款。不加兩側銀線、不加底部銀珠，只用中間長孔吊起玉牌，讓糯冰底和飄綠色帶成為主角。",
        "direction": "做 925 銀耳勾小牌耳墜。銀色耳勾接小圈及短接件，穿過中間長孔上方固定，保持玉牌自然垂直。",
        "process": "左右配對檢查 - 檢查中間長孔內壁及孔口 - 配 925 銀耳勾、小圈及短接件 - 穿過中孔上方固定 - 確認左右高度、擺動和磨孔風險 - 拍上耳和近鏡。",
        "copy": "糯冰底上有一筆自然飄綠，像水墨線條落在冰感玉面。銀色中孔耳勾做法最乾淨，保留玉牌本身形狀和透感。",
        "ig": "這對最美的是那一筆綠。不要側框，也不要底珠，只用銀色耳勾從中孔吊起，讓糯冰飄綠自己乾淨地發光。",
        "price": "HK$880-1280",
        "shoot": "飄綠近鏡、中孔接駁近鏡、上耳垂墜、白衫清爽感、與 M010 深飄綠對比。",
        "renders": [
            ("首選：銀色中孔簡潔耳勾款", "M009/product-09-silver-ear-hook-real-material-reference.png"),
        ],
        "worn": ("配戴預想：銀色中孔耳勾上耳", "M009/worn-01-silver-ear-hook-slot.png"),
    },
    {
        "id": "M010",
        "name": "糯冰深飄綠牌仔耳環",
        "category": "第二批 / 飄綠耳飾系列",
        "photo": "M010-IMG_5891.JPG",
        "size": "15.0 x 10.9 x 3.0mm",
        "cost": "5件總價945 CNY，單件未分配",
        "decision": "首選金色中孔簡潔耳勾款。不加兩側金線、不加底部金珠，用金色耳勾襯深綠飄花，令款式更成熟但仍然乾淨。",
        "direction": "做金色耳勾小牌耳墜。金色耳勾接小圈及短接件，穿過中間長孔上方固定，讓深綠玉牌自然垂下。",
        "process": "檢查左右花色是否平衡 - 檢查中間長孔內壁及孔口 - 配金色耳勾、小圈及短接件 - 穿過中孔上方固定 - 確認左右高度、擺動和磨孔風險 - 上耳拍攝。",
        "copy": "糯冰底裡有集中深綠飄花，小小一對但很有存在感。配金色耳勾後更成熟，金色襯深綠花色，乾淨但有貴氣。",
        "ig": "比 M009 更深一點、更穩一點。金色耳勾從中孔吊起，不加側線和底珠，讓深綠飄花成為剛剛好的亮點。",
        "price": "HK$880-1280",
        "shoot": "深綠花近鏡、中孔接駁近鏡、黑衫/白衫上耳、與 M009 系列照。",
        "renders": [
            ("首選：金色中孔簡潔耳勾款", "M010/product-06-gold-ear-hook-slot-only-actual-proportion.png"),
        ],
        "worn": ("配戴預想：金色中孔耳勾上耳", "M010/worn-01-gold-ear-hook-slot.png"),
    },
    {
        "id": "M011",
        "name": "糯冰灰黑牌仔耳環",
        "category": "第二批 / 中性耳飾系列",
        "photo": "M011-IMG_5895.JPG",
        "size": "12.8 x 9.1 x 3.0mm",
        "cost": "5件總價945 CNY，單件未分配",
        "decision": "灰黑花色較中性，適合用黑銀、氧化銀或槍黑色五金去呼應烏雞灰黑紋理。主方向不要太甜美，保留冷調、低調和中性感。",
        "direction": "做短耳墜系列比較：槍黑 huggie 較沉穩有份量；氧化銀耳勾較輕身、冷感較明顯。",
        "process": "左右深色花紋配對 - 檢查孔位及邊角 - 測槍黑 huggie 與氧化銀耳勾 - 確認整體比例不要過幼稚 - 拍中性穿搭。",
        "copy": "灰黑糯冰小牌，像一小片冷調石紋。配黑銀或氧化銀後更沉穩，適合不想戴太綠翡翠的人。",
        "ig": "灰黑色的翡翠有另一種安靜感。黑銀和氧化銀把烏雞紋理壓得更穩，不甜、不高調，像日常裡一點冷冷的石紋。",
        "price": "HK$780-1080",
        "shoot": "黑 Tee/白 Tee 上耳、中性穿搭、灰黑紋理近鏡、與 M003 煙墨色呼應。",
        "renders": [
            ("槍黑 huggie 短耳墜", "M011/product-04-gunmetal-huggie-slot-drop.png"),
            ("氧化銀耳勾款", "M011/product-05-oxidized-silver-ear-hook-slot-drop.png"),
        ],
        "worn": ("配戴預想：槍黑 huggie 上耳", "M011/worn-01-gunmetal-huggie-slot.png"),
    },
    {
        "id": "M012",
        "name": "糯冰灰白黑紋幾何吊墜",
        "category": "第二批 / 圖案感小吊墜",
        "photo": "M012-IMG_5899.JPG",
        "size": "14.0 x 10.9 x 2.3mm",
        "cost": "5件總價945 CNY，單件未分配",
        "decision": "單件小牌，灰白底配黑色線紋，圖案感強。薄身邊角適合用全包邊保護；銀色包邊較乾淨，黑色包邊更 graphic、更中性。",
        "direction": "做全包邊幾何小吊墜，保留黑色線紋作主視覺。銀色版本偏清爽日常；黑色版本呼應玉內黑紋，視覺更鮮明。",
        "process": "確認最適合朝向 - 檢查厚度及邊角 - 按形狀做全包邊 - 配小圈及幼鏈 - 確認吊墜重心 - 拍近鏡線紋。",
        "copy": "灰白糯冰底上帶黑色線紋，像天然畫出的小小圖案。全包邊後更完整，低調但很有個性。",
        "ig": "這件不是靠綠取勝，而是靠線條。灰白糯冰底、黑色自然紋，被一圈細邊框起來，像一枚很小的石紋圖案吊墜。",
        "price": "HK$580-780",
        "shoot": "線紋近鏡、白底商品照、黑衫上頸、與 M011 灰黑系列合照。",
        "renders": [
            ("銀色 true bezel 壓邊小吊墜", "M012/product-05-silver-true-bezel-lip.png"),
            ("黑色 true bezel 壓邊小吊墜", "M012/product-06-black-true-bezel-lip.png"),
        ],
        "worn": ("配戴預想：銀色全包邊上頸", "M012/worn-01-full-silver-bezel-necklace.png"),
    },
]


def p(text, style):
    return Paragraph(str(text).replace("\n", "<br/>"), style)


def report_image_path(path):
    path = Path(path)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    out = ASSET_DIR / f"{path.stem}-report.jpg"
    if out.exists() and out.stat().st_mtime >= path.stat().st_mtime:
        return out

    with PILImage.open(path) as im:
        im = im.convert("RGB")
        im.thumbnail((1500, 1500), PILImage.Resampling.LANCZOS)
        im.save(out, "JPEG", quality=86, optimize=True, progressive=True)
    return out


def img_flowable(path, max_w, max_h):
    path = Path(path)
    image_path = report_image_path(path)
    with PILImage.open(image_path) as im:
        w, h = im.size
    scale = min(max_w / w, max_h / h)
    return Image(str(image_path), width=w * scale, height=h * scale)


def make_table(data, col_widths, style):
    wrapped = [[p(cell, style) for cell in row] for row in data]
    table = Table(wrapped, colWidths=col_widths, hAlign="LEFT", repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dfe7e1")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#25312d")),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#c9d0ca")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def render_grid(item, small):
    cells = []
    row = []
    count = len(item["renders"])
    max_w = 66 * mm if count <= 2 else 44 * mm
    max_h = 48 * mm if count <= 2 else 26 * mm
    col_width = 84 * mm if count <= 2 else 55 * mm

    for idx, (label, rel_path) in enumerate(item["renders"]):
        path = RENDER_DIR / rel_path
        block = [
            img_flowable(path, max_w, max_h),
            Spacer(1, 2 * mm),
            p(label, small),
        ]
        row.append(block)
        if len(row) == (2 if count <= 2 else 3):
            cells.append(row)
            row = []

    if row:
        while len(row) < (2 if count <= 2 else 3):
            row.append("")
        cells.append(row)

    table = Table(cells, colWidths=[col_width] * (2 if count <= 2 else 3), hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return table


def render_worn(item, small):
    label, rel_path = item["worn"]
    path = RENDER_DIR / rel_path
    block = [
        img_flowable(path, 60 * mm, 38 * mm),
        Spacer(1, 2 * mm),
        p(label, small),
    ]
    table = Table([[block]], colWidths=[84 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return table


def item_summary_table(item, small):
    rows = [
        ["分類", item["category"]],
        ["尺寸", item["size"]],
        ["成本", item["cost"]],
        ["建議售價", item["price"]],
        ["成品方向", item["direction"]],
        ["拍攝重點", item["shoot"]],
    ]
    return make_table(rows, [24 * mm, 128 * mm], small)


def build_pdf():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(TTFont(PDF_FONT_NAME, PDF_FONT_PATH))

    styles = getSampleStyleSheet()
    base = ParagraphStyle(
        "BaseCJK",
        parent=styles["Normal"],
        fontName=PDF_FONT_NAME,
        fontSize=9.2,
        leading=13.2,
        textColor=colors.HexColor("#27312e"),
        alignment=TA_LEFT,
        spaceAfter=4,
    )
    title = ParagraphStyle("TitleCJK", parent=base, fontSize=28, leading=36, alignment=TA_CENTER, spaceAfter=12)
    subtitle = ParagraphStyle("SubtitleCJK", parent=base, fontSize=14, leading=21, alignment=TA_CENTER)
    h1 = ParagraphStyle("H1CJK", parent=base, fontSize=16, leading=22, spaceBefore=8, spaceAfter=7)
    h2 = ParagraphStyle("H2CJK", parent=base, fontSize=12.2, leading=17, spaceBefore=6, spaceAfter=4)
    small = ParagraphStyle("SmallCJK", parent=base, fontSize=8.1, leading=11.2, textColor=colors.HexColor("#5a625f"))
    callout = ParagraphStyle("CalloutCJK", parent=base, fontSize=10.2, leading=15.5, textColor=colors.HexColor("#25312d"))

    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title="現貨成品化計劃書",
    )

    story = []
    story.append(Spacer(1, 34 * mm))
    story.append(p("現貨成品化計劃書", title))
    story.append(p("M001-M012 翡翠現貨：產品設計、加工、拍攝及 IG 上架文案", subtitle))
    story.append(Spacer(1, 12 * mm))
    story.append(p("日期：2026-07-24<br/>版本：合併第一批 M001-M007 及第二批 M008-M012，加入 M004 / M007 / M012 最新修正成品圖及已確認設計偏好<br/>定位：現代簡約、日常高質感、HK$500-1500 入門至主力價格帶", callout))
    story.append(Spacer(1, 12 * mm))
    story.append(p("核心判斷", h1))
    story.append(p("兩批現貨可以合併成三條清晰產品線：日常吊墜、輕盈耳飾、灰墨中性。第一批 M001-M007 已有較多設計探索；第二批 M008-M012 更適合快速變成耳飾和小吊墜系列。M004 主推 half bezel / side prong 迷你戒指；M005 主推短銀針加貼石小銀珠；M007 首選短銀針固定珠組耳線；M009/M010 首選中孔簡潔耳勾小牌款，M012 作 graphic 小吊墜補充。", callout))
    story.append(PageBreak())

    story.append(p("1. 成品化總覽", h1))
    overview = [
        ["分類", "對應貨品", "成品方向", "優先"],
        ["快速上架", "M007", "灰月甜甜圈耳線，首選短銀針固定珠組，確認 925 銀耳線後拍攝", "高"],
        ["第二批耳飾", "M008-M011", "糯冰平安扣及中孔簡潔小牌耳飾，可組成淡綠/深綠對照", "高"],
        ["主力日常", "M002", "無事牌項鏈，按鏈款測銀鏈/皮繩/蠟繩 tone", "高"],
        ["中性測款", "M003", "煙墨甜甜圈吊墜，黑繩方向較強", "中"],
        ["透光小吊墜", "M001", "open-back / floating support，避免貼皮膚失透", "中"],
        ["孔位小吊墜", "M005, M006", "M005 側肩孔用短銀針；M006 正頂中央互通孔測銀鏈/蠟繩", "中"],
        ["迷你戒指", "M004", "主推 02 half bezel / side prong 戒面款", "中"],
        ["圖案感吊墜", "M012", "灰白黑紋幾何小牌，銀鏈小吊墜", "中"],
    ]
    story.append(make_table(overview, [31 * mm, 29 * mm, 90 * mm, 21 * mm], base))
    story.append(p("設計偏好紀錄", h2))
    story.append(p("已確認：M004 的 02 half bezel / side prong 幾啱心水，之後作主設計方向。M005 已確認用短銀針加兩邊貼石小銀珠連銀鏈。M007 已確認短銀針固定珠組耳線為首選款。M009 已確認銀色中孔簡潔耳勾款；M010 已確認金色中孔簡潔耳勾款。暫定：M001 的 Style 02 或 Style 03 較好。", base))
    story.append(p("建議時間表", h2))
    timeline = [
        ["階段", "行動", "產出"],
        ["Day 1-2", "逐件 QC、確認孔位/裂/厚度、確認配件材質", "QC 表、加工清單"],
        ["Day 3-7", "M002/M007 先拍攝；M008-M011 配同系列耳圈；M005/M006 測配件；M004 問戒指鑲嵌報價", "第一輪可拍成品"],
        ["Week 2", "決定 M001 托起方式、M003 主推繩款、M004 戒托細節、M012 吊墜扣法", "可上架 SKU 和加工單"],
        ["Week 3", "完成商品相、上身/上耳相、IG caption A/B test", "正式上架素材"],
    ]
    story.append(make_table(timeline, [28 * mm, 78 * mm, 65 * mm], base))
    story.append(PageBreak())

    story.append(p("2. 逐件產品方案及成品圖", h1))
    for idx, item in enumerate(ITEMS):
        photo_path = PHOTO_DIR / item["photo"]
        item_block = [
            p(f'{item["id"]} - {item["name"]}', h1),
            Table(
                [[img_flowable(photo_path, 36 * mm, 43 * mm), item_summary_table(item, small)]],
                colWidths=[42 * mm, 130 * mm],
                hAlign="LEFT",
                style=[
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ],
            ),
            p("設計決策", h2),
            p(item["decision"], callout),
            p("成品設計圖", h2),
            render_grid(item, small),
            p("配戴預想圖", h2),
            render_worn(item, small),
            p("加工方法", h2),
            p(item["process"], base),
            p("產品文案", h2),
            p(item["copy"], base),
            p("IG Caption 草稿", h2),
            p(item["ig"], callout),
        ]
        story.extend(item_block)
        if idx != len(ITEMS) - 1:
            story.append(PageBreak())

    story.append(PageBreak())
    story.append(p("3. IG 上架內容計劃", h1))
    ig_rows = [["SKU", "Post 角度", "Caption Hook", "CTA"]]
    for item in ITEMS:
        hook = item["ig"].split("。")[0] + "。"
        ig_rows.append([item["id"], item["category"], hook, "DM 查詢尺寸/保留現貨"])
    story.append(make_table(ig_rows, [18 * mm, 43 * mm, 80 * mm, 30 * mm], small))
    story.append(p("建議發佈節奏", h2))
    story.append(p("先發 M007、M008-M011，因為耳飾最快像正式商品，亦容易做成系列內容；再發 M002 作主力日常項鏈。M009/M010 可做淡飄綠與深飄綠對照；M011 與 M003 可放入灰墨中性線；M005 以短銀針小銀珠作設計亮點；M004 用戒指設計過程作故事；M001 用透光結構解釋為何要把玉托起。", base))

    story.append(p("4. 拍攝 Shot List", h1))
    shot_rows = [
        ["類型", "目的", "每件必拍"],
        ["白底商品相", "IG catalog 清楚展示", "正面、側面、背面、尺寸比例"],
        ["黑底/透光相", "突出透度、飄花、棉絮和輪廓", "近鏡、透光、孔位/扣頭"],
        ["上身/上耳相", "令客人理解大小和日常感", "白衫、黑衫各一張"],
        ["細節相", "建立信任和材質披露", "孔位、鑲口、鏈扣、厚度、瑕疵位置"],
    ]
    story.append(make_table(shot_rows, [32 * mm, 60 * mm, 79 * mm], base))

    story.append(p("5. 風險及下一步", h1))
    risks = [
        ["風險", "處理方法"],
        ["裂、崩、孔位磨損未確認", "加工前先用放大鏡和強光逐件 QC，拍照留底"],
        ["配件材質影響質感", "M002、M007 如非 925 銀，建議換配件再上架；M007 需確認短銀針珠組焊位或小圈結構穩固"],
        ["M005/M006 孔位磨線", "確認孔口有無利邊；M006 需按正頂中央互通孔選合適線徑，必要時先拋孔"],
        ["第二批總價未分配", "M008-M012 上架前要按實際價值和加工成本分配單件成本"],
        ["成對耳飾左右差異", "M008-M011 要確認大小、厚薄、花色和垂墜高度是否平衡"],
        ["M004 戒托成本過高", "只問簡約 half bezel / side prong，不做複雜鑲嵌"],
        ["M001 貼膚失透", "採用 open-back / floating support，拍攝時加入透光對比"],
    ]
    story.append(make_table(risks, [48 * mm, 123 * mm], base))

    story.append(PageBreak())
    story.append(p("6. CAD 加工圖 Appendix", h1))
    story.append(p("以下 CAD-style 圖集中放在 PDF 底部，用作工場報價、確認孔位/扣位、五金顏色、受力點、磨孔及刮手風險。M004 和 M012 已特別標示不能只靠外框視覺，需有實際壓邊 / 爪位 / 底托固定。", callout))
    for idx, item in enumerate(ITEMS):
        label, path = CAD_DIAGRAMS[item["id"]]
        story.append(KeepTogether([
            p(f'{item["id"]} - {label}', h2),
            img_flowable(path, 170 * mm, 170 * mm),
        ]))
        if idx != len(ITEMS) - 1:
            story.append(PageBreak())

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(PDF_FONT_NAME, 8)
    canvas.setFillColor(colors.HexColor("#6f7773"))
    canvas.drawString(16 * mm, 8 * mm, "Jade Inventory Product Plan")
    canvas.drawRightString(194 * mm, 8 * mm, f"Page {doc.page}")
    canvas.restoreState()


if __name__ == "__main__":
    build_pdf()
    print(PDF_PATH)
