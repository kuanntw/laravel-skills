---
name: laravel-vibe
description: 為 Laravel、Livewire 與 Filament 專案提供版本分流、實作與驗收指引。適用於新增功能、API、資料層、多租戶權限與回歸測試；保留繁體中文 short-first、i18n 與 on-premise 治理。
---

# Laravel Vibe

這是薄入口，不取代既有規範，也不增加工具權限。

1. 先讀 [SKILLS_INDEX.md](SKILLS_INDEX.md)，只載入本次需要的模組。僅在維護原始 repository 時，若 repository 根目錄存在 `WORKFLOW.md`，先讀其維護規範並遵循「索引 → skill → 模板 → README → workflow」順序；獨立安裝此 skill 不依賴套件外檔案。
2. 開工先走 [版本偵測與分流](00-core/version-detection-and-routing.md)：以目標專案 composer.lock 與既有結構為準，未知先確認，不預設最新版。
3. 涉及資源存取時，走 [授權與租戶測試](30-quality/authorization-and-tenant-tests.md) 及 [安全驗收矩陣](templates/security-acceptance-matrix.md)。validation 成功不代表有權操作。
4. 保留 [short-first 多語系](16-i18n/multilingual-strategy.md)、[租戶翻譯覆蓋](16-i18n/tenant-translation-override.md) 與 [外部資源 / on-premise 政策](00-core/static-assets-and-external-resources.md)。
5. 依 [品質閘門](30-quality/testing-and-quality.md) 與 [PR checklist](templates/pr-checklist.md) 交付版本證據、測試結果、未執行項及回滾方式。

Laravel Boost 僅作為版本感知與官方文件查詢的參考。不得因載入本 skill 自動安裝套件、啟用 MCP、執行資料庫操作、升級框架或改變原有授權範圍。來源與授權處理見 [參考來源](references/upstream-sources.md)。
