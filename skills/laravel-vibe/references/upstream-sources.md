# 官方參考來源與授權

查閱日期：2026-10-25。以下是本次指引的依據，不代表每個專案都應升到當日最新版本。實作時依 `composer.lock` 選同版本文件，核對小版本 API；主分支與文件可能繼續變更。

- [Laravel Boost 官方 repository](https://github.com/laravel/boost) 與 [官方 Boost 文件](https://laravel.com/docs/13.x/boost)：專案版本資訊、依已安裝套件查文件、guidelines / skills 分工的參考。本套件不是 Boost、不是其 fork，也不取代專案的既有規則。
- [Composer lock 說明](https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies)：lock 記錄解析後版本，與 composer.json 約束不同。
- [Laravel 11 application structure 升級說明](https://laravel.com/docs/11.x/upgrade#application-structure)：升級不要求搬移舊結構。
- [Laravel 12 授權](https://laravel.com/docs/12.x/authorization)、[Form Request 授權與驗證](https://laravel.com/docs/12.x/validation#authorizing-form-requests)、[Eloquent mass assignment](https://laravel.com/docs/12.x/eloquent#mass-assignment)、[query builder](https://laravel.com/docs/12.x/queries#introduction)：權限、欄位允許清單及查詢欄位不能依賴參數綁定的依據；其他版本須對照同 major 文件。
- [Livewire 2→3 升級](https://livewire.laravel.com/docs/3.x/upgrading)、[3→4 升級](https://livewire.laravel.com/docs/4.x/upgrading)、[Livewire 4 security](https://livewire.laravel.com/docs/4.x/security)：版本差異、公開屬性與 action 必須視為可遭竄改的輸入。
- [Filament 官方文件版本選單](https://filamentphp.com/docs/5.x/introduction/installation)：先切換到 lock 相同 major，不以連結中的 5.x 視為專案版本。

## 重用界線

本次新增的說明、Python helper、測試與驗收範例皆為本 repository 撰寫，未複製 Boost 的 Blade 模板或上游程式碼。引用來源不會把本 repository 自動改成 MIT，也不在此替原 repository 宣告新授權。

Boost 使用 [MIT license](https://github.com/laravel/boost/blob/main/LICENSE.md)。未來若實際複製或改寫其程式碼 / 模板，必須記錄來源檔案與精確 commit，並隨重用內容保留上游著作權聲明及完整 MIT notice；不能只保留此連結。外部素材仍須依本套件既有 on-premise 與授權治理處理。
