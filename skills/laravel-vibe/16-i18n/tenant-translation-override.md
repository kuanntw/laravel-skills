# Skill 17 — Tenant Translation Override

## 目的
支援 SaaS 多租戶在不改主程式的前提下覆蓋翻譯文案。

## 覆蓋層級（類繼承）
1. Tenant override
2. Product default
3. Framework fallback

## 檔案/資料建議
- 預設語系：`lang/{locale}/*.php`
- 租戶覆蓋：`lang/tenants/{tenant_id}/{locale}/*.php`（或 DB 字典）

## 載入策略
1. 載入 product default dictionary
2. 載入 tenant dictionary
3. 同 key 以 tenant 值覆蓋
4. 缺漏 key 回退到 default

## 風險控制
- 產出 missing keys 報告
- 限制可覆蓋 key 範圍（避免核心系統訊息被誤改）
- 記錄租戶翻譯變更審計（who/when/what）

## 測試建議
- 同一 key 在不同 tenant 顯示不同內容
- tenant 未定義 key 時可正確 fallback
- 租戶切換後語系內容立即生效

