# Laravel Vibe Coding Skills Kit

這個 repository 提供一套可重複引用的 **PHP Laravel 技能模組（skills）**，目標是讓你在做 vibe coding（快速、互動、偏產品導向的開發）時，有一套穩定的「調研 → 規劃 → 實作 → 驗證 → 交付」參考框架。

## 你會得到什麼

- 一份標準 [SKILL.md](skills/laravel-vibe/SKILL.md) 薄入口：載入既有索引與規範，不改變工具權限。
- 一份 `SKILLS_INDEX.md`：總覽所有 skill 的用途、觸發時機、輸出格式。
- 一份 `WORKFLOW.md`：規範未來每次調整 skill 時的更新流程與 PR 最低要求。
- Laravel Core 技能模組（架構、API、資料層、靜態資源與外部 CDN 治理、品質、交付、AI 協作）。
- Livewire 專用技能模組（元件設計、表單與列表、測試、效能）。
- Livewire / Filament 選型討論指引，避免把底層互動框架與後台 UI framework 混用。
- i18n 多語系技能模組（短文案策略、語系預設、租戶覆蓋翻譯）。
- 可複用模板（需求澄清、實作計畫、PR checklist、Livewire 任務模板、操作手冊模板）。
- 參考 Laravel Boost 的 composer.lock 版本分流，以及只讀、無額外依賴的版本偵測 helper。
- allowed / denied / cross-tenant 安全測試指引、HTTP 測試起手式與可填寫的驗收矩陣。

## 快速使用方式（建議）

1. 由 [SKILL.md](skills/laravel-vibe/SKILL.md) 進入，先讀 `skills/laravel-vibe/SKILLS_INDEX.md`。若要調整 skill 體系，先讀 `WORKFLOW.md` 按 SOP 更新。
2. 先做 [版本偵測與分流](skills/laravel-vibe/00-core/version-detection-and-routing.md)，按目標專案 composer.lock 與既有慣例選文件，不預設最新版、不自動安裝 Boost 或升級套件。
3. 若任務涉及圖片、字型、CSS/JS、外部 CDN asset 或 on-premise 部署限制，先走 `00-core/static-assets-and-external-resources.md`。
4. 如果需求可能用 Livewire 或 Filament 實作，先和使用者討論選型：Livewire 是 Laravel 的底層動態 UI component 框架；Filament 是建立在 Livewire 上的 admin panel / forms / tables / dashboards UI framework。
5. 如果確認是 Blade + Livewire 任務，優先走 `12-livewire/*` skills，範例須核對相同 major。
6. 若有多語系需求，先走 `16-i18n/*` 並使用 `templates/i18n/i18n-rollout-checklist.md`，保留繁體中文 short-first。
7. 先用 `templates/implementation-plan.md` 或 `templates/livewire/livewire-task-template.md` 產出計畫；涉及資源存取時填寫 [安全驗收矩陣](skills/laravel-vibe/templates/security-acceptance-matrix.md)。
8. 完成後依 `30-quality/testing-and-quality.md` + `30-quality/spec-consistency-and-coverage.md` 跑 spec 一致性與 coverage 檢查，並依 [授權與租戶測試](skills/laravel-vibe/30-quality/authorization-and-tenant-tests.md) 驗證未授權 / 跨租戶操作、mass assignment、排序與篩選 allowlists。
9. 補齊 `templates/operation-manual-template.md` 產出操作手冊。
10. 用 `templates/pr-checklist.md` 做交付前檢查，分開報告已跑、失敗與未跑項目。

## 可重複驗證

在本 repository 根目錄執行（Python 3.9+，只用標準函式庫）：

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

細節見 [測試說明](tests/README.md)。這些檢查只驗證版本 helper、入口、索引與文件連結，不等於 Laravel application tests。HTTP 範例與驗收矩陣須在目標專案的 PHP / vendor / 隔離測試 DB 完成實際驗證。

官方版本依據與授權處理見 [來源說明](skills/laravel-vibe/references/upstream-sources.md)。此套件不複製 Boost Blade 模板、不宣告新的 repository 授權，也不擴張原有工具權限。

## 適用情境

- 新功能快速孵化（MVP）
- 既有 Laravel 專案的增量開發
- API-first 專案
- Laravel + Livewire 互動式後台/內部系統
- 需要判斷應使用 Livewire 自行組 UI，或使用 Filament 快速建立後台、表單、資料表與 dashboard
- 需要把 AI 生成程式碼納入團隊規範

## 維護建議

- 每次改 skill 前先更新索引，再改內容。
- 若流程或規範有變動，務必同步更新 `WORKFLOW.md`。
- 讓模板與 skill 內容保持一致，避免文件與實務脫節。

## Revision History

### 2026-10-25

- 新增標準 `SKILL.md` 薄入口，保留 `SKILLS_INDEX.md` 與既有維護流程。
- 新增 composer.lock-first 版本偵測及 Laravel / Livewire / Filament 分流；參考 Laravel Boost 官方來源，不自動安裝、升級或複製 Blade 模板。
- 新增 allowed / denied / cross-tenant 測試指引、HTTP 測試起手式與 13 項安全驗收矩陣，涵蓋 authorization ≠ validation、mass assignment、排序 / 篩選 allowlists 及無未授權副作用。
- 同步 API、資料層、Livewire、品質門檻與計畫 / PR 模板，維持繁體中文 short-first、i18n 與 on-premise 政策。
- 新增無第三方 Python 依賴的 GitHub Actions repository 驗證流程；確認 skill 內連結可獨立安裝，並防止 HTTP 範例因 Unicode-escaped JSON 漏掉租戶資料洩漏。
- 驗證：25 項 Python repository-local tests 通過；`git diff --check` 通過。此環境無 PHP，且本 repository 不是 Laravel application，未執行 PHP 語法檢查、Artisan、application suite、Pint 或 PHPStan；未宣稱實際業務安全測試已通過。

