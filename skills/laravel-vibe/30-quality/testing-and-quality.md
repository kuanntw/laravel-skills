# Skill 30 — Testing & Quality Gate

## 目的
以最小成本建立可回歸的信心，避免 vibe coding 產生隱性風險。

## 最低測試組合（建議）
1. **Feature tests**：核心 user flow（成功 + 失敗各一）
2. **Unit tests**：商業規則（價格、狀態轉移、權限判斷）
3. **API contract tests**：關鍵欄位與錯誤碼

## Laravel 實務
- 使用 `RefreshDatabase` 維持隔離。
- factories 建立最小可讀資料。
- 測試命名採 Given/When/Then 語意。

## 品質閘門（PR 前）
- `php artisan test` 全綠
- 靜態分析（Larastan/PHPStan）至少 baseline 無新增錯誤
- 格式化（Pint）已執行

## 輸出
- Test Matrix（Case / Type / Priority）
- 風險遺留清單（允收理由 + 後續計畫）

