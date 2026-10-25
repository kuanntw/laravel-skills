# Template — 安全驗收矩陣

## 先填契約
- Feature / spec / commit：
- Laravel / Livewire / Filament / PHPUnit 或 Pest 的 lock 版本與文件 URL：
- Actor / guard / tenant membership / tenant context 建立方式：
- Policy / gate / route binding / scope：
- Allowed 成功碼或 UI 結果：
- Guest 結果（JSON 401 或明確的 web redirect）：
- 同租戶 denied 狀態：
- Cross-tenant 狀態（固定選定 403 或 404，不允許測試接受兩者）：
- 非法欄位 / 排序 / 篩選：拒絕或安全預設的明確契約：
- Bulk 混合合法 / 非法 ID：全筆拒絕或逐筆授權契約：
- 測試 DB、外部服務 fake / 隔離方法：

A / B 為不同租戶；A-editor 有該操作權，A-viewer 無該操作權。每個適用 action 各複製一份矩陣，不以單一 update case 宣稱整個系統覆蓋。

| AC | 情境與操作 | 必須斷言 | Test file / case | 結果 / 證據 |
|---|---|---|---|---|
| AUTH-01 allowed | A-editor + A resource + 合法 payload | 明確成功結果；預期欄位正確，tenant / owner 正確；預期副作用一次 | 待填 | 未跑 |
| AUTH-02 denied | A-viewer + A resource + 同一合法 payload，直接呼叫 endpoint / action | 明確拒絕；資料、ownership、筆數不變；無未授權副作用 | 待填 | 未跑 |
| AUTH-03 guest | 未登入直接呼叫受保護 action | 401 或指定 redirect；無內容洩漏 / 異動 / 副作用 | 待填 | 未跑 |
| VAL-01 validation | A-editor + A resource + 不合法 payload | 明確 validation error（JSON 通常 422），欄位錯誤符合 spec；無異動 | 待填 | 未跑 |
| TEN-01 cross-tenant | A-editor 以 B 的 route / nested resource ID 讀寫，B→A 也測 | 固定 403 或 404；不洩漏對方內容；原資料及筆數不變；無副作用 | 待填 | 未跑 |
| TEN-02 identity tamper | 偽造 header / query / body tenant、owner、relation ID 或 Livewire public property | 拒絕或忽略依契約；不能改 tenant context、指向 B 關聯或繞過 action 授權 | 待填 | 未跑 |
| TEN-03 collection | A 搜尋、排序、翻頁、統計、匯出 / 下載 | 僅 A 的 IDs、內容、總數、檔案；結果不能混入 B | 待填 | 未跑 |
| TEN-04 bulk / import | 合法 A ID 混入 B ID，含匯入其中一列 | 依明確 atomic / partial 契約；B 絕不讀寫，失敗行無副作用 | 待填 | 未跑 |
| TEN-05 context reuse | 同一 session / worker / cache A→B→A，若有翻譯覆蓋一併測 | context 隔離；cache、背景工作、翻譯不串租戶 | 待填 | 未跑 |
| MASS-01 create | 合法建立 payload 加 tenant_id / owner_id / role / is_admin / 巢狀敏感欄位 | 依拒絕 / 忽略契約；server-owned 值可信，不能越權建立 | 待填 | 未跑 |
| MASS-02 update | 合法更新 payload 加上述欄位 | 敏感欄位前後相同；若允許一般欄位更新，也不提升權限 | 待填 | 未跑 |
| QUERY-01 allowlist | 允許 sort / direction / filter / page size | 明確順序、結果與分頁；仍只含目前 tenant | 待填 | 未跑 |
| QUERY-02 denylist probes | 未知欄位、敏感欄位、SQL 片段、非法 direction / operator、過大分頁、filter[tenant_id]=B | 明確拒絕或安全預設；非 500、無 SQL / 資料洩漏、無擴權 | 待填 | 未跑 |

## 證據
- Focused 命令與結果：
- 完整 suite / 靜態分析 / 格式檢查命令與結果：
- 未跑、失敗、不適用：原因 / 風險 / 下一步：
- Coverage 範圍（不得以模板或文件檢查當作應用程式測試 coverage）：
- 回滾 / 操作手冊連結：
