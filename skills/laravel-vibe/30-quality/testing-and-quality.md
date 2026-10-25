# Skill 30 — Testing & Quality Gate

## 目的
以最小成本建立可回歸的信心，避免 vibe coding 產生隱性風險。

## 最低測試組合（建議）
1. **Feature tests**：核心 user flow（allowed、denied、validation fail；多租戶另加 cross-tenant）
2. **Unit tests**：商業規則（價格、狀態轉移、權限判斷）
3. **API contract tests**：關鍵欄位與錯誤碼

## Laravel 實務
- 使用 `RefreshDatabase` 維持隔離。
- factories 建立最小可讀資料。
- 測試命名採 Given/When/Then 語意。
- 先完成 [版本分流](../00-core/version-detection-and-routing.md)，沿用已安裝 runner 與測試慣例，不新增執行期依賴。
- `RefreshDatabase` 前確認為隔離測試 DB，不操作正式資料。
- 權限與租戶案例依 [Skill 32](authorization-and-tenant-tests.md) / [安全驗收矩陣](../templates/security-acceptance-matrix.md)，不能用 validation error 代替 denied，也要檢查無資料異動 / 副作用。

## 品質閘門（PR 前）
- `php artisan test` 全綠
- 靜態分析（Larastan/PHPStan）至少 baseline 無新增錯誤
- 格式化（Pint）已執行

使用專案已有且可執行的工具；缺 PHP / vendor / DB / 分析工具時，明列「未跑」與原因，不臨時安裝或宣稱通過。本 skills repository 的文件與 helper 測試使用 `python3 -m unittest discover -s tests -v`，不是 Laravel application suite。

## 輸出
- Test Matrix（Case / Type / Priority）
- 風險遺留清單（允收理由 + 後續計畫）

