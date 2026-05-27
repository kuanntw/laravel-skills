# Skill 20 — Data & Eloquent

## 目的
在快速開發下，避免資料模型失控或查詢效能惡化，並且確保資料庫變更可持續演進（不可依賴反覆清空 DB）。

## Migration 原則
1. **禁止用清空資料庫取代 schema 維護**：每次欄位/索引/約束變更都要新增 migration，避免直接 drop/recreate 作法。
2. migration 要可重複執行（idempotent）且支援 rollback，必要時加防呆判斷（例如欄位存在檢查）。
3. 先定義資料生命週期（建立、更新、刪除、封存）。
4. 索引以查詢模式為導向，不是欄位越多越好。
5. foreign key 明確，必要時設定 cascade 規則。
6. 正式環境資料修正優先走 migration + seeder/command，不走手動 SQL。

## Admin 帳號維運（reset-admin）
當專案需要重設管理員密碼時，應提供可審計且可重複使用的 script/command，而非直接改資料庫。

### reset-admin 腳本要求
1. 採 **互動式流程**：先讀取現有 admin 帳號清單，顯示可選項。
2. 若清單非空：可選擇其中一個 admin 並重設 password。
3. 若清單為空：引導建立第一個 admin（最少包含 name/email/password）。
4. 密碼輸入需遮罩，不要明文回顯；重設後要輸出結果摘要（成功/失敗）。
5. 將此腳本納入操作手冊（指令、前置條件、常見錯誤）。

### 建議實作形式（Laravel）
- 優先使用 Artisan Command（例如 `php artisan app:reset-admin`）。
- 以 role 欄位、permission 或指定 guard 辨識 admin 身分。
- 搭配 `Hash::make()` 寫入密碼，禁止明文儲存。

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
- Migration 清單（含每次變更原因）
- 每張表的索引策略
- 高風險查詢與預估資料量
- Admin 維運指令（含 reset-admin 使用說明）
