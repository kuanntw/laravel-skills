# Skill 15 — Livewire Performance & Pitfalls

## 常見坑
- 每次輸入都觸發昂貴查詢
- component 過大導致 re-render 成本高
- N+1 問題在 render/query 中反覆出現

## 優化策略
1. 善用 `wire:model.blur` 或 debounce
2. 拆小 component，減少不必要重繪
3. 查詢先 `with()` 預載關聯
4. 重資料列表使用快取或 query 優化
5. 事件只傳必要 payload

## 觀測指標
- 首次互動延遲
- 搜尋輸入延遲
- 分頁切換時間
- 5xx 與 validation 失敗率

