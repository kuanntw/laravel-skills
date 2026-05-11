# Skill 40 — Release & Observability

## 目的
確保功能可上線、可監控、可回滾。

## 發版前
1. 確認 migration 是否可逆。
2. feature flag（若有）預設值安全。
3. 例外通知通道（Slack / Email / APM）可用。

## 上線策略
- 低風險：直接部署 + smoke test
- 中風險：分批 rollout
- 高風險：dark launch + 指標觀察

## 監控最低集
- 錯誤率（5xx）
- 延遲（P95/P99）
- 核心業務指標（例如建立訂單成功率）

## 回滾條件
- 連續 10 分鐘錯誤率超標
- 核心流程成功率低於警戒值
- 資料一致性出現破壞

## 輸出
- Release Checklist
- Smoke Test Steps
- Rollback Runbook（3~5 步）

