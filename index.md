# Jade Project Hub

最後更新：2026-08-23

這裡是 GitHub / GitHub Pages 友善版本的 project 入口，用來快速查看 inventory、產品構思、品牌資料和工作文件。

## Quick Links

| Section | 用途 |
| --- | --- |
| [Visual Inventory](inventory.md) | 圖片版現貨清單，適合直接在 GitHub 當網站瀏覽 |
| [Material Inventory](trackers/material-inventory.md) | 完整入貨紀錄、成本、尺寸、狀態 |
| [Product Ideas](trackers/inventory-product-ideas.md) | 逐件產品方向、售價帶、拍攝方向 |
| [Project Brief](knowledge-base/00-project-brief.md) | 品牌定位和 project 背景 |
| [Roadmap](knowledge-base/01-six-month-roadmap.md) | 6 個月進度規劃 |
| [Weekly Tracker](knowledge-base/02-weekly-task-tracker.md) | 每週 task board |
| [Finished Product QC](knowledge-base/12-finished-product-qc-checklist.md) | 成品上架前 QC checklist |
| [Photography Workflow](knowledge-base/13-product-photography-workflow.md) | 商品拍攝流程 |
| [Copywriting](copywriting/README.md) | IG / FAQ / care note 文案 |
| [PDF Reports](output/pdf/) | 已輸出的 inventory / product plan PDF |

## Project Structure

```text
.
├── index.md                         # GitHub Pages / website entry
├── inventory.md                     # visual inventory gallery
├── README.md                        # repo overview
├── knowledge-base/                  # strategy, roadmap, decisions, workflows
├── trackers/                        # inventory, product ideas, trip reviews, images
│   ├── material-inventory.md
│   ├── inventory-product-ideas.md
│   ├── images/
│   └── concept-renders/
├── copywriting/                     # reusable shop and content copy
├── templates/                       # reusable markdown templates
├── scripts/                         # report generation scripts
└── output/                          # PDFs, brand assets, generated visuals
```

## GitHub Pages Setup

In GitHub repo settings, set Pages source to:

- Branch: `main` or your active branch
- Folder: `/ (root)`

Using root as the Pages folder keeps image paths like `trackers/images/...` working without copying assets into a separate docs folder.

