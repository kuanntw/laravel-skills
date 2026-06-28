# Skill 12 — Livewire Component Architecture

## 目的
建立可維護的 Livewire 元件邊界，避免把商業邏輯塞進 component。

## 與 Filament 的選型邊界
開始設計前，應先和使用者確認要使用 Livewire 還是 Filament，避免把兩者定位混在一起：

- **Livewire**：Laravel 的底層互動框架，讓開發者用 PHP 撰寫動態 UI component，減少大量前端 JavaScript。
- **Filament**：建立在 Livewire 上的 Laravel UI framework，主要用於快速建立後台、forms、tables、dashboards。

若需求是高度客製的前台互動或需要自行掌控 component 結構，優先使用 Livewire；若需求是標準化後台 CRUD、資料表、表單或 dashboard，應先評估 Filament。

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

