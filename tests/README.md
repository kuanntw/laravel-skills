# Repository-local validation

在 repository 根目錄執行，使用 Python 3.9+ 標準函式庫，不安裝 runtime dependency：

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

- `test_detect_versions.py`：lock 優先、Laravel 10 / 11 / 12 / 13 分流、Livewire / Filament、dev 依賴、缺檔 / 格式 / 重複項 / 非穩定版本 / 未知 major / 不一致版本、CLI exit code、只讀行為。
- `test_repository.py`：薄入口、索引完整性、相對文件連結、skill 獨立安裝可攜性、安全驗收列及 JSON 洩漏檢查範例的內容回歸檢查。
- `fixtures/*.json`：人造、最小 lock 片段，僅測解析與選路，不是可安裝的完整 lock，也不是套件相容性證明。
- 測試不連外、不執行 Composer / Artisan、不建立 Laravel application，不驗證 PHP 範例語法或應用程式行為。
- 實際 feature / tenant / authorization 測試須在目標 application 的正確版本與隔離測試 DB 執行，依 [安全驗收矩陣](../skills/laravel-vibe/templates/security-acceptance-matrix.md) 保存證據。
