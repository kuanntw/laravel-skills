# Laravel Vibe Coding Skills Kit

這個 repository 提供一套可重複引用的 **PHP Laravel 技能模組（skills）**，目標是讓你在做 vibe coding（快速、互動、偏產品導向的開發）時，有一套穩定的「調研 → 規劃 → 實作 → 驗證 → 交付」參考框架。

## 你會得到什麼

- 一份 `SKILLS_INDEX.md`：總覽所有 skill 的用途、觸發時機、輸出格式。
- 一份 `WORKFLOW.md`：規範未來每次調整 skill 時的更新流程與 PR 最低要求。
- Laravel Core 技能模組（架構、API、資料層、品質、交付、AI 協作）。
- Livewire 專用技能模組（元件設計、表單與列表、測試、效能）。
- i18n 多語系技能模組（短文案策略、語系預設、租戶覆蓋翻譯）。
- 可複用模板（需求澄清、實作計畫、PR checklist、Livewire 任務模板、操作手冊模板）。

## 快速使用方式（建議）

1. 開工前先讀 `skills/laravel-vibe/SKILLS_INDEX.md`。
2. 若要調整 skill 體系，先讀 `WORKFLOW.md` 按 SOP 更新。
3. 如果是 Blade + Livewire 任務，優先走 `12-livewire/*` skills。
4. 若有多語系需求，先走 `16-i18n/*` 並使用 `templates/i18n/i18n-rollout-checklist.md`。
5. 先用 `templates/implementation-plan.md` 或 `templates/livewire/livewire-task-template.md` 產出計畫。
6. 完成後依 `30-quality/testing-and-quality.md` + `30-quality/spec-consistency-and-coverage.md` 跑 spec 一致性與 coverage 檢查。
7. 補齊 `templates/operation-manual-template.md` 產出操作手冊。
8. 用 `templates/pr-checklist.md` 做交付前檢查。

## 適用情境

- 新功能快速孵化（MVP）
- 既有 Laravel 專案的增量開發
- API-first 專案
- Laravel + Livewire 互動式後台/內部系統
- 需要把 AI 生成程式碼納入團隊規範

## 維護建議

- 每次改 skill 前先更新索引，再改內容。
- 若流程或規範有變動，務必同步更新 `WORKFLOW.md`。
- 讓模板與 skill 內容保持一致，避免文件與實務脫節。

