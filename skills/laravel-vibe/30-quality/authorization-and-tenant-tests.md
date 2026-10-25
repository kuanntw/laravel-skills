# Skill 32 — Authorization & Tenant Tests

## 目的
讓「可操作、不可操作、不可跨租戶」各自有可重跑證據；不能只驗證 UI 按鈕隱藏或輸入格式錯誤。

## 步驟
1. 先完成 [版本分流](../00-core/version-detection-and-routing.md)，使用專案既有 PHPUnit / Pest 與 Livewire 測試 API。
2. 定義 actor、guard、tenant context、resource、action、policy / gate，以及固定的拒絕狀態。JSON guest 通常為 401，web guest 可能導向登入；無權限與跨租戶依專案選定 403 或隱藏資源的 404。每條測試只能斷言選定的結果，不寫「403 或 404 都算過」。
3. 用獨立測試 DB / connection 建立 tenant A、tenant B、A 的 editor / viewer、B 的 editor，與各自資料。`RefreshDatabase` 只能作用在已確認的測試環境，不對 production 跑 migration / reset。
4. 對每個 read / create / update / delete / bulk / export / import action 建立 allowed、denied、cross-tenant 案例，按 [安全驗收矩陣](../templates/security-acceptance-matrix.md) 選適用列。不可只測 policy unit test，還要直接呼叫 HTTP endpoint / Livewire action。
5. denied 與 cross-tenant 使用**合法 payload**，確保失敗來自授權，不是 validation。另用有權限 actor + 不合法 payload 測 validation。表單 `authorize()`、policy / gate、tenant scope 與 validation 各有責任，`validated()` 不會自動授權。
6. 所有拒絕案例斷言無資料異動與無未授權副作用：筆數、原資料與 ownership 不變；相關 job / mail / notification / 業務事件不送出；檔案未建立、webhook 未呼叫。只 fake 本案例的外部副作用，不把待測 policy / tenant middleware / scope mock 成永遠通過，也不要 fake 全部 model events 而繞過租戶 observer。
7. 保存測試命令、commit、實際結果與未跑原因；文件模板通過不等於應用程式安全測試已通過。

## 必測邊界

### Authorization ≠ validation
- 已登入不等於有權限；同租戶也不等於有權限。測一般使用者嘗試管理員 action，以及 valid payload 被拒絕。
- 隱藏按鈕、disabled 欄位、Livewire locked 屬性都不是 server-side policy 的替代品。直接 `call()` / 發 HTTP request 測試；mount 的授權不取代後續 action 授權。
- `exists` / `unique` 如需 tenant 隔離，必須限制 tenant。驗證 foreign key 存在不代表它屬於目前租戶。

### Tenant 隔離
- tenant context 來自可信的登入 / membership 流程，不直接信任 request 的 `tenant_id`、header、query 或 Livewire public property。
- 測 route ID、nested relation ID、body ID、bulk IDs、匯入每列的外租戶 ID；用 A actor 存取 B 資料，再反向測 B→A。
- 列表、搜尋、排序、分頁、count / aggregation、匯出與下載均不能洩漏 B 的 ID、內容、總數或檔案。關聯查詢與 `orWhere` 也不能脫離 tenant 條件。
- 若有跨租戶管理員，必須獨立定義授權、稽核與測試，不默認一般 admin 可跨租戶。
- 若有快取、queue / 長駐 worker、翻譯覆蓋或租戶切換，依序 A→B→A 操作，確認 context / cache key 不串租戶，背景任務明確攜帶並重建正確 context。

### Mass assignment
- 測注入 `tenant_id`、`owner_id`、`role`、`is_admin` 以及巢狀敏感欄位。建立與更新都要覆蓋。
- 專案可選拒絕欄位或明確忽略，但必須固定契約並斷言敏感值未變；不能把 HTTP 200 當成安全證據。
- 使用明確輸入允許清單與模型 `$fillable` / `$guarded`。tenant / owner 等 server-owned 值由可信 context 指派。不得用 `$request->all()` / 未過濾 Livewire state 直接 `create()`、`fill()`、`update()`，也不靠關閉 guarding 讓測試變綠。

### Sorting / filtering allowlists
- 用固定 map 把公開 sort key 映射到允許欄位；direction 只允許 `asc` / `desc`。filter key、operator、value 型別與範圍、page size 皆有白名單 / 上限。
- 測合法排序的順序與合法篩選的結果；再測未知 key、受保護欄位、raw SQL 片段、非法 direction / operator、過大分頁與 `filter[tenant_id]=B`。
- 非法輸入應依明確契約拒絕或採安全預設，且不得擴大資料範圍。參數綁定保護的是值，不是 column name；不可直接將 request sort 傳入 `orderByRaw`。

## 輸出與完成條件
- 已填寫的 [安全驗收矩陣](../templates/security-acceptance-matrix.md)，每個適用 AC 有測試檔 / case 名稱及結果。
- 核心三路徑範例見 [HTTP 測試起手式](../templates/authorization-test-example.md)；必須改成目標專案的模型、欄位、路由、guard 與測試版本才能執行。
- 不適用項記錄理由，不能因為「目前沒有 UI 按鈕」就略過 server action。
- 仍遵守繁體中文 short-first、i18n fallback、on-premise 與既有權限範圍。來源見 [官方參考](../references/upstream-sources.md)。
