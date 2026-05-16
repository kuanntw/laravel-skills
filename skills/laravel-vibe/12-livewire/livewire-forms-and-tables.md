# Skill 13 — Livewire Forms & Tables

## 目的
快速交付常見 CRUD 互動：表單、搜尋、排序、分頁。

## 表單模式
- `wire:model.live`：即時更新（欄位少、互動即時）
- `wire:model.blur`：失焦更新（降低請求數）
- `wire:submit.prevent`：統一送出入口

## 列表模式
- 只要是資料量可能偏大的列表，一律啟用分頁（預設使用 `WithPagination`）
- 搜尋條件變更時 `resetPage()`
- 查詢集中在 computed / query builder method

## 匯入/匯出規範
- 匯出資料功能必須支援 `xlsx`
- 匯入資料功能必須同時支援 `csv` 與 `xlsx`

## 實作清單
1. 輸入防呆（trim、型別轉換）
2. 成功訊息（toast/flash）
3. 錯誤訊息（欄位 + 全域）
4. loading skeleton
5. 空狀態文案
6. 列表分頁（大資料量時不可省略）
7. 匯入/匯出格式檢查（`csv`/`xlsx`）

