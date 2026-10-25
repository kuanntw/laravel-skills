# Template — PR Checklist

## Scope
- [ ] 變更範圍符合本次需求
- [ ] 無不必要檔案修改
- [ ] 版本依 composer.lock 及既有慣例分流，未強制升級或自行安裝 Boost / 啟用新工具權限

## Code Quality
- [ ] 無重大重複邏輯
- [ ] 錯誤處理與回應格式一致
- [ ] 無硬編碼敏感資訊
- [ ] 靜態資源盡可能使用相對路徑或專案 asset pipeline
- [ ] 若使用外部 CDN asset，已確認 on-premise / 內網 / 離線需求並記錄替代方案

## Tests
- [ ] Feature tests 已覆蓋主要流程
- [ ] 失敗路徑已測試
- [ ] 測試在本地可通過
- [ ] [安全驗收矩陣](security-acceptance-matrix.md) 已填寫：allowed / denied / cross-tenant，另測 validation
- [ ] 拒絕案例使用合法輸入；DB、ownership 與外部副作用不變
- [ ] mass assignment、排序 / 篩選 allowlist、直接呼叫 action 已覆蓋
- [ ] 已列實際命令與結果；未跑或不適用項有理由，不以文件檢查冒充 application test

## Release
- [ ] migration 風險已評估
- [ ] rollback 方案已定義
- [ ] 監控/告警已確認

