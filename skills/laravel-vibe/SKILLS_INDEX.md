# SKILLS_INDEX — Laravel Vibe Coding

> 目標：讓每次 Laravel 開發都能快速進入可執行狀態，同時保持可維護性。

## Skill 地圖

| 編號 | Skill | 何時使用 | 主要輸出 |
|---|---|---|---|
| 00 | `project-framing` | 需求模糊、剛起案 | 需求邊界、風險與里程碑 |
| 10 | `feature-architecture` | 要切分功能模組與責任 | 模組切分、路由/Controller/Service 設計 |
| 11 | `api-design` | 要定義 REST API | endpoint 規格、驗證規則、錯誤格式 |
| 20 | `data-and-eloquent` | 需要 schema 與 Eloquent | migration、關聯、query 策略 |
| 30 | `testing-and-quality` | 寫完功能要驗證 | 測試矩陣、最低測試清單 |
| 40 | `release-and-observability` | 準備上線與維運 | 發版 checklist、監控與 rollback |
| 50 | `ai-collaboration-playbook` | AI 共寫流程治理 | Prompt 模板、審查規則、風險控管 |

## 使用原則

1. **先定義 Done，再開始寫 Code**。
2. **每次只引入最少必要 skill**，避免流程過重。
3. **每個 skill 的輸出都要落地到檔案**（不是只留在對話）。
4. **測試與回滾方案必須成對出現**。

## 推薦流程（快速版）

1. `00 project-framing`
2. `10 feature-architecture` + `11 api-design`
3. `20 data-and-eloquent`
4. 實作
5. `30 testing-and-quality`
6. `40 release-and-observability`

