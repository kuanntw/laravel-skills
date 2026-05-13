# Skill 11 — API Design (REST in Laravel)

## 目的
建立一致、可測試、可擴展的 API 規格，讓前後端與 AI 協作更順。

## 規格基準
- 資源命名使用複數：`/users`, `/orders`
- 操作語義依 HTTP method
- 錯誤格式統一：`code`, `message`, `details`
- 分頁統一：`meta` + `links`

## 設計清單
1. Endpoint 一覽（method/path/用途）
2. Request 驗證規則（Laravel validation）
3. Response schema（成功 / 失敗）
4. 權限矩陣（角色對 endpoint）
5. 版本策略（必要時 `/api/v1`）

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

