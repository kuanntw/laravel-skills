# Template — PR Checklist

## Scope
- [ ] 變更範圍符合本次需求
- [ ] 無不必要檔案修改

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

## Release
- [ ] migration 風險已評估
- [ ] rollback 方案已定義
- [ ] 監控/告警已確認

