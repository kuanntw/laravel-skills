# Skill 31 — Spec Consistency & Unit Test Coverage

## 目的
確保開發過程中，需求規格、實作行為、與測試驗證保持一致。

## 一致性檢查（三對齊）
1. **Spec ↔ API/UI**：欄位、狀態、錯誤碼一致
2. **Spec ↔ Domain Rules**：商業規則與邊界條件一致
3. **Spec ↔ Tests**：每條 AC 至少對應一個測試案例

## Coverage 規範（最低）
- Unit tests 覆蓋核心商業規則
- 新增/修改的 service 或 action 必須有 unit tests
- 建議 PR 附上變更範圍 coverage 摘要（至少核心模組）

## PR 必附內容
- Spec 版本或連結
- AC 對應測試矩陣
- Coverage 摘要（模組/範圍）

## 反模式
- 只更新程式碼不更新 spec
- 只跑整體 test，不確認關鍵規則 coverage
- PR 無法追蹤 spec 與測試關聯

