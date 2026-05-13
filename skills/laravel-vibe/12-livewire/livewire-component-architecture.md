# Skill 12 — Livewire Component Architecture

## 目的
建立可維護的 Livewire 元件邊界，避免把商業邏輯塞進 component。

## 元件分層
- **Page Component**：頁面級協調（查詢條件、分頁、佈局狀態）
- **Feature Component**：單一互動功能（例如建立訂單表單）
- **UI Fragment Component**：可重用小區塊（tag selector、status badge）

## 結構建議
- `app/Livewire/{Domain}/{Feature}/...`
- `resources/views/livewire/{domain}/{feature}/...`
- 複雜邏輯抽到 `Action/Service`，component 只做狀態與呼叫。

## 規範
1. component 公開屬性要有清楚命名與預設值。
2. validation 規則集中於 `rules()` 或 Form Object。
3. 事件命名統一（`order-created`, `filter-updated`）。
4. 每個 component 要定義 loading、empty、error UI。

