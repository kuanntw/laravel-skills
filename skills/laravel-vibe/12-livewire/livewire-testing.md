# Skill 14 — Livewire Testing

## 目的
確保 Livewire 互動流程可回歸，不只測 happy path。

## 最低測試
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
- 主要元件至少 1 成功 + 1 失敗案例
- 分頁/搜尋元件至少 1 條件切換案例

