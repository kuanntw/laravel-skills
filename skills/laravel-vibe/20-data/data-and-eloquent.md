# Skill 20 — Data & Eloquent

## 目的
在快速開發下，避免資料模型失控或查詢效能惡化。

## Migration 原則
1. 先定義資料生命週期（建立、更新、刪除、封存）。
2. 索引以查詢模式為導向，不是欄位越多越好。
3. foreign key 明確，必要時設定 cascade 規則。

## Eloquent 關聯規範
- 優先使用明確命名關聯：`customer()`, `items()`。
- N+1 預防：預先 `with()` 載入。
- 跨多層關聯查詢前，先寫測試再優化。

## Query 策略
- 複雜條件用 query scope。
- 可重用統計查詢抽到 Read Model / Query Service。
- 資料量大時，使用 chunk/cursor。

## 輸出模板
- ER 簡圖（文字可）
- Migration 清單
- 每張表的索引策略
- 高風險查詢與預估資料量

