# SKILLS_INDEX — Laravel Vibe Coding

> 目標：讓每次 Laravel 開發都能快速進入可執行狀態，同時保持可維護性。

## Skill 地圖

| 編號 | Skill | 何時使用 | 主要輸出 |
|---|---|---|---|
| 00 | `project-framing` | 需求模糊、剛起案 | 需求邊界、風險與里程碑 |
| 01 | `static-assets-and-external-resources` | 涉及圖片、字型、JS/CSS、CDN 或 on-premise 部署限制 | 靜態資源策略、外部資源風險與本地化方案 |
| 10 | `feature-architecture` | 要切分功能模組與責任 | 模組切分、路由/Controller/Service 設計 |
| 11 | `api-design` | 要定義 REST API | endpoint 規格、驗證規則、錯誤格式 |
| 12 | `livewire-component-architecture` | Livewire 頁面分層與責任切分 | component 結構與狀態邊界 |
| 13 | `livewire-forms-and-tables` | Livewire CRUD 互動頁 | 表單/搜尋/分頁實作清單 |
| 14 | `livewire-testing` | 寫完 Livewire 元件要驗證 | component 測試矩陣 |
| 15 | `livewire-performance-and-pitfalls` | 遇到延遲或重繪過多 | 效能優化與避坑指引 |
| 16 | `multilingual-strategy` | 導入多語系與短文案策略 | key 命名、fallback、語系優先序 |
| 17 | `tenant-translation-override` | SaaS 租戶需覆蓋翻譯 | tenant 覆蓋層與治理規範 |
| 20 | `data-and-eloquent` | 需要 schema 與 Eloquent | migration、關聯、query 策略 |
| 30 | `testing-and-quality` | 寫完功能要驗證 | 測試矩陣、最低測試清單 |
| 31 | `spec-consistency-and-coverage` | 需強化 spec 對齊與 unit coverage | AC 對應矩陣、coverage 摘要 |
| 40 | `release-and-observability` | 準備上線與維運 | 發版 checklist、監控與 rollback |
| 41 | `operation-manual` | 交付後需要可操作文件 | 操作手冊與排障指引 |
| 50 | `ai-collaboration-playbook` | AI 共寫流程治理 | Prompt 模板、審查規則、風險控管 |

## 使用原則

1. **先定義 Done，再開始寫 Code**。
2. **先討論 Livewire / Filament 選型，避免混亂**：Livewire 是 Laravel 的底層互動 component 框架，讓團隊用 PHP 撰寫動態 UI、減少大量前端 JavaScript；Filament 是建立在 Livewire 上的 Laravel UI framework，適合快速建立 admin panel、forms、tables、dashboards。
3. **每次只引入最少必要 skill**，避免流程過重。
   - 若任務涉及靜態資源、外部 CDN asset 或部署環境限制，必須納入 `01 static-assets-and-external-resources`。
4. **每個 skill 的輸出都要落地到檔案**（不是只留在對話）。
5. **測試與回滾方案必須成對出現**。

## 推薦流程（Laravel + Livewire / Filament）

1. `00 project-framing`：先確認要用 Livewire 自行組互動 UI，或用 Filament 做後台 / 表單 / 資料表 / dashboard。
2. `01 static-assets-and-external-resources`（若涉及靜態資源 / CDN / on-premise）
3. `10 feature-architecture`
4. `12 livewire-component-architecture` + `13 livewire-forms-and-tables`
5. `16 multilingual-strategy` + `17 tenant-translation-override`
6. `20 data-and-eloquent`
7. 實作
8. `14 livewire-testing` + `30 testing-and-quality` + `31 spec-consistency-and-coverage`
9. `15 livewire-performance-and-pitfalls`
10. `40 release-and-observability` + `41 operation-manual`

