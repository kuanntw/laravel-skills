# Template — i18n Rollout Checklist

## A. 字串策略
- [ ] 關鍵 UI key 已提供 `short`
- [ ] 長文案已拆成 `long`
- [ ] 超短空間元件有 `abbr`

## B. 語系預設與儲存
- [ ] 已實作語系優先序（DB > Cookie > localStorage > Browser > Default）
- [ ] 使用者切換語系會同步更新 Cookie
- [ ] 使用者切換語系會同步更新 localStorage
- [ ] 登入後可將選擇同步到使用者設定

## C. 租戶覆蓋
- [ ] 支援 tenant dictionary 覆蓋 default dictionary
- [ ] 缺漏 key 會 fallback
- [ ] 有 missing keys 報告
- [ ] 有覆蓋 key 白名單或保護機制

## D. 驗證
- [ ] 同頁在不同語系不破版
- [ ] 同語系在不同租戶可顯示不同文案
- [ ] 切換 tenant / locale 不需清快取即可生效（或有明確快取策略）

