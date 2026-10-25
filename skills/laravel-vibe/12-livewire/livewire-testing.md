# Skill 14 — Livewire Testing

## 目的
確保 Livewire 互動流程可回歸，不只測 happy path。

## 最低測試
先走 [版本分流](../00-core/version-detection-and-routing.md)。下列事件 assertion 範例適用 Livewire 3；v2 使用其既有 `assertEmitted` 等 API，v4 依官方同版本文件確認，不為測試範例升級套件。

1. `Livewire::test()` 驗證 mount 初始狀態
2. 設定欄位 + 呼叫 action
3. 驗證 validation error
4. 驗證資料寫入與事件 dispatch

## 範例重點
- `set('form.email', 'invalid')` + `call('save')`
- `assertHasErrors(['form.email' => 'email'])`
- `assertDispatched('order-created')`
- `assertSee('建立成功')`

## 品質門檻
- 主要元件至少 allowed、denied（合法輸入）、validation fail；多租戶另有 cross-tenant
- 分頁/搜尋元件至少 1 條件切換案例
- 直接呼叫 public action，不只驗證按鈕隱藏；竄改 resource ID / tenant ID / sort / filter 後仍受 server-side 授權與 allowlist 保護。
- mount 的授權與 locked property 不能取代 action 內的授權；拒絕後斷言 DB 與副作用不變。
- 依 [安全驗收矩陣](../templates/security-acceptance-matrix.md) 覆蓋表單、刪除、列表、bulk 與匯入 / 匯出等適用操作。

