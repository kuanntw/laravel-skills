# Skill 11 — API Design (REST in Laravel)

## 目的
建立一致、可測試、可擴展的 API 規格，讓前後端與 AI 協作更順。

## 規格基準
- 資源命名使用複數：`/users`, `/orders`
- 操作語義依 HTTP method
- 錯誤格式統一：`code`, `message`, `details`
- 列表只要可能有大量資料，一律提供分頁（回應統一 `meta` + `links`）
- 資料匯出端點至少支援 `xlsx`
- 資料匯入端點需同時支援 `csv` 與 `xlsx`

## 設計清單
1. Endpoint 一覽（method/path/用途）
2. Request 驗證規則（Laravel validation）
3. Response schema（成功 / 失敗）
4. 權限矩陣（角色對 endpoint）
5. 版本策略（必要時 `/api/v1`）

## 授權與資料邊界
- 開工先做 [版本分流](../00-core/version-detection-and-routing.md)；API URL 版本不等於 Laravel 套件版本。
- Authentication、authorization、validation 分開處理。FormRequest 的 `rules()` / `validated()` 不取代 policy / gate；同租戶也需檢查 action 權限。
- Tenant context 與 server-owned 欄位不可直接取自客戶端輸入；route binding、關聯、列表與匯出都需租戶範圍。
- Sort key / direction、filter key / operator / value 與 page size 使用明確允許清單，不把使用者欄位名直接交給 SQL。
- 依 [安全驗收矩陣](../templates/security-acceptance-matrix.md) 定義 allowed、denied、cross-tenant、mass assignment 與非法查詢結果。

## JSON 回應建議
```json
{
  "code": "OK",
  "message": "success",
  "data": {}
}
```

錯誤：
```json
{
  "code": "VALIDATION_ERROR",
  "message": "The given data was invalid.",
  "details": {
    "email": ["The email field is required."]
  }
}
```

