# 2026-08-19 Product Photos

用途：產品相 backup 及後續 PDF、ideas.md、IG 上架、成品圖參考。

來源：`/Users/astronaut/Downloads`

## Storage Structure

| Folder | Purpose |
| --- | --- |
| `originals/heic/` | iPhone HEIC 原檔 backup |
| `originals/jpg/` | 原本已是 JPG 的 group layout 相 |
| `converted/jpg/` | HEIC 轉出的 JPG 版本，方便一般文件使用 |
| `converted/png/` | HEIC 轉出的 PNG 版本，方便預覽、裁圖及圖像處理 |
| `by-tag/` | 按用途及視覺 tag 建立的 symlink 分類，不重複儲存實體檔 |

## Tag Folders

| Tag Folder | Meaning |
| --- | --- |
| `by-tag/overview-layout/` | 多件貨同框 layout / inventory overview |
| `by-tag/product-closeup/` | 單件或少量產品 close-up |
| `by-tag/finished-earrings/` | 已完成耳環成品相 |
| `by-tag/color-white-icy/` | 白冰 / 糯冰 / 淡色件 |
| `by-tag/color-green/` | 青綠 / 飄綠件 |
| `by-tag/color-grey-black/` | 灰黑 / 烏雞 / 水墨感件 |
| `by-tag/color-yellow-honey/` | 黃翡 / 蜜糖色件 |

## Manifest

| Original | Converted | Category | Tags | Notes |
| --- | --- | --- | --- | --- |
| `originals/heic/IMG_9158.HEIC` | `converted/jpg/IMG_9158.jpg`, `converted/png/IMG_9158.png` | product close-up | `product-closeup`, `color-white-icy` | 白底帶黃翡點的大平安扣 / 甜甜圈近照 |
| `originals/heic/IMG_9160.HEIC` | `converted/jpg/IMG_9160.jpg`, `converted/png/IMG_9160.png` | product close-up | `product-closeup`, `color-grey-black` | 灰黑長方牌 close-up，頂部有孔 |
| `originals/heic/IMG_9163.HEIC` | `converted/jpg/IMG_9163.jpg`, `converted/png/IMG_9163.png` | product close-up | `product-closeup`, `color-green` | 深青綠長方牌 close-up |
| `originals/heic/IMG_9165.HEIC` | `converted/jpg/IMG_9165.jpg`, `converted/png/IMG_9165.png` | finished product | `finished-earrings`, `color-green` | 飄綠牌仔耳環成品 close-up |
| `originals/heic/IMG_9169.HEIC` | `converted/jpg/IMG_9169.jpg`, `converted/png/IMG_9169.png` | finished product | `finished-earrings`, `color-green` | 飄綠牌仔耳環成品 close-up |
| `originals/heic/IMG_9177.HEIC` | `converted/jpg/IMG_9177.jpg`, `converted/png/IMG_9177.png` | product close-up | `product-closeup`, `color-yellow-honey` | 黃翡水滴 / 馬眼形件 close-up |
| `originals/heic/IMG_9178.HEIC` | `converted/jpg/IMG_9178.jpg`, `converted/png/IMG_9178.png` | product close-up | `product-closeup`, `color-yellow-honey` | 黃翡水滴 / 馬眼形件 close-up |
| `originals/jpg/IMG_6333.jpg` | N/A | overview layout | `overview-layout` | 多件貨同框排版相 |
| `originals/jpg/IMG_6334.jpg` | N/A | overview layout | `overview-layout` | 多件貨同框排版相 |
| `originals/jpg/IMG_6335.jpg` | N/A | overview layout | `overview-layout` | 多件貨同框排版相 |
| `originals/jpg/IMG_6336.jpg` | N/A | overview layout | `overview-layout` | 多件貨同框排版相 |
| `originals/jpg/IMG_6337.jpg` | N/A | overview layout | `overview-layout` | 多件貨同框排版相 |

## Notes

- 原始 filename 已保留，方便追溯到 iPhone / Downloads 原相。
- `by-tag/` 入面的檔案是 symlink；若要編輯相片，請使用 `converted/` 或 `originals/` 入面的實體檔。
- HEIC 已轉 JPG 及 PNG；日常放 PDF / markdown 用 JPG，做視覺檢查或圖像處理用 PNG。
