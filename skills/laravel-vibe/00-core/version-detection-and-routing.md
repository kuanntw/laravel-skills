# Skill 02 — Version Detection & Routing

## 目的
先確認「專案實際鎖定什麼」，再選對版本的文件與測試寫法。參考 Laravel Boost 的專案資訊與文件查詢方式，但 Boost 不是必要依賴。

## 步驟
1. 讀目標專案 `composer.lock` 的 `packages` 與 `packages-dev`，記錄 `laravel/framework`、`livewire/livewire`、`filament/filament` / `filament/panels`，以及已採用的 Pest / PHPUnit、Boost 版本。`composer.json` 的 `^12.0` 是相容範圍，不是已解析版本；lock 也不是目前 vendor / runtime 已同步的證明。
2. 可使用本套件的只讀 helper（Python 3.9+ 標準函式庫，無 PHP 或第三方依賴）：
   ```sh
   python3 /path/to/laravel-skills/skills/laravel-vibe/scripts/detect_versions.py /path/to/application
   ```
   只讀該路徑的 `composer.lock`。exit 0 表示必要版本可分流；exit 2 表示缺檔、格式錯誤、缺 Laravel、重複記錄、開發版或尚無對應指引，必須確認。輸出不包含 lock 內的 repository URL、憑證或其他套件內容。
3. 對照 `composer.json`、現有測試、`bootstrap/app.php`、`app/Http/Kernel.php`、provider / policy 註冊、Livewire namespace 與 Filament panel 設定。不依目錄形狀反推版本，也不為了配合範例改專案結構。
4. 若已有可用且獲准的 Boost，按其實際可用工具讀 Application Info，透過 Search Docs 取得對應套件版本文件。它可能連到 hosted 文件服務；on-premise 禁止連外時改用已核准的本地文件，不傳專案資料到外部服務。不自動安裝 Boost 或啟用其其他工具。
5. lock 缺失、dev branch / alias / prerelease、套件間不一致、runtime 與 lock 衝突時，標為「待確認」。先用本地已安裝 metadata / 已有版本證據釐清，不以最新版填空，不執行 `composer update` 來解決資訊不足。若需要執行 Artisan 等會載入專案程式的命令，遵守原有執行權限與環境限制。

## 版本分流

| 偵測結果 | 採用方式 | 不可直接套用 |
|---|---|---|
| Laravel 10 | 讀 10.x 文件及現有 Kernel / provider / middleware 註冊方式 | 11+ 新專案的 bootstrap 設定 |
| Laravel 11 | 讀 11.x 文件；新 skeleton 與舊結構均可能存在。官方升級指引不要求把 10.x 結構改成新 skeleton | 把「11」當成必須重建目錄 |
| Laravel 12 或 13 | 分別讀 12.x 或 13.x 文件，保留該專案既有結構，逐項核對涉及的 API | 把 13.x 範例直接貼到 12.x，或只憑 major 判定所有小版本 API 可用 |
| 其他 Laravel major / 無法辨識 | 查該版本官方文件與專案既有用法，記錄人工確認；helper 保守回報待確認 | 假裝不支援就升級，或默認 13 |
| Livewire 2 | 讀 2.x 文件；沿用專案 `emit` / `assertEmitted` 等 v2 測試慣例 | v3 的 `dispatch` / `assertDispatched`、`.live` 範例 |
| Livewire 3 | 讀 3.x 文件；事件已改用 `dispatch` / `assertDispatched`，model 同步修飾詞依 3.x 核對 | 把 v2 的預設同步行為視為不變 |
| Livewire 4 | 讀 4.x 文件及 3→4 升級差異，確認元件形式、設定、路由與測試 API；`.blur` / `.change` 要保留 v3 的網路更新行為時核對 `.live` | 因為是 v4 就搬動既有元件、升級 Filament，或假設 model 修飾詞語意不變 |
| Filament 2 / 3 / 4 / 5 | 由官方版本選單選中 lock 相同 major，核對 resource / action / panel / tenancy API 及該版本需求 | 從 Laravel major 推算 Filament major，或混貼不同版本 namespace |
| 未安裝 Livewire / Filament / Boost | 標「未出現在 lock」，略過該套件專屬指引；依需求討論選型 | 自動安裝、宣稱套件必然在 runtime 缺失 |

這是文件選路表，不是套件相容性或安全支援期限保證。若已過官方支援期，另列風險與選項，不在功能任務中強制升級。

## 輸出
- 套件精確 lock 版本 / 來源、目標 PHP 約束與可取得的 runtime 證據（兩者分開）
- 已核對的既有結構與對應官方文件 URL / major / 查閱日期
- 已知不一致、待確認事項、採用或略過的 skill
- 測試 runner 與可執行命令，明確區分「已跑 / 失敗 / 未跑」

官方來源與授權說明：[upstream-sources.md](../references/upstream-sources.md)。
