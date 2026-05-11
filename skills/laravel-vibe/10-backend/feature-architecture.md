# Skill 10 — Feature Architecture (Laravel)

## 目的
把需求轉成 Laravel 中可維護的結構：Route → Controller → Action/Service → Model/Repository。

## 建議分層
- **Route**：僅做路由綁定與 middleware。
- **Controller**：請求協調、回應格式。
- **FormRequest**：輸入驗證與授權。
- **Action/Service**：核心商業邏輯（可測試）。
- **Model/Eloquent**：資料關聯與簡單 domain 行為。

## 設計規範
1. Controller 方法不超過 30~40 行。
2. 業務規則不可散落在 Controller。
3. 外部整合（支付、郵件、第三方 API）透過 adapter 封裝。
4. 以 feature folder 組織（必要時）而非純技術層分散。

## 輸出模板
- Use Case 名稱
- 主要流程（3~7 步）
- 例外流程
- 類別清單（責任 + 介面）
- 非功能需求（效能、安全、可觀測）

## 參考目錄（示意）
```text
app/
  Http/Controllers/Billing/SubscriptionController.php
  Http/Requests/Billing/CreateSubscriptionRequest.php
  Actions/Billing/CreateSubscriptionAction.php
  Services/BillingGateway/StripeGateway.php
  Models/Subscription.php
```

