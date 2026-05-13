# Skill 50 — AI Collaboration Playbook (Laravel)

## 目的
把 AI 從「會吐 code 的工具」提升為「可治理的工程協作者」。

## 工作模式
1. **Spec-first**：先讓 AI 產規格，再產程式碼。
2. **Small-batch**：每次只改 1 個 use case。
3. **Human Gate**：人類審核 domain rule、資安、資料風險。

## Prompt 模板（精簡）
- 背景：專案目標與角色
- 任務：這次只做哪個 use case
- 限制：不改 schema / 只改 API / 保持相容
- 驗收：測試案例與預期輸出

## 審查重點
- 有沒有把邏輯塞進 controller？
- 驗證規則是否集中在 FormRequest？
- 錯誤碼、回應格式是否一致？
- 測試是否覆蓋失敗路徑？

## 常見失誤
- 一次生成太多檔案，難以審查
- 忽略 migration 風險
- 只測 happy path

