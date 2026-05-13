# Skill 16 — Multilingual Strategy (Short-first UI)

## 目的
在中文主導介面中導入多語系，同時避免文字過長造成 UI 破版。

## 文案設計原則
1. **Short-first**：UI 預設使用短文案。
2. 每個 key 建議提供 `short / long / abbr` 三種層級。
3. Button/Tab/Badge 優先使用 `short`，Tooltip/說明使用 `long`。
4. 目標是「語義正確 + 長度可控」，不是逐字翻譯。

## Key 命名建議
- `domain.feature.item.short`
- `domain.feature.item.long`
- `domain.feature.item.abbr`

範例：
- `billing.plan.short = 方案`
- `billing.plan.long = 訂閱方案設定`
- `billing.plan.abbr = 案`

## 語系決策優先序
1. 使用者 profile 設定（DB）
2. Cookie（server 可讀）
3. localStorage（client）
4. 瀏覽器 `Accept-Language`
5. 系統預設（例如 `zh-TW`）

## 輸出
- i18n key 命名表
- 字串長度準則（按元件類型）
- 語系 fallback 規格

