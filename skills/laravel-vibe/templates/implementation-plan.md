# Template — Implementation Plan

## Use Case

## 目標

## 技術方案
- 版本證據：composer.lock 的 Laravel / Livewire / Filament / test runner 精確版本；PHP 約束與 runtime 證據分開
- 相同 major 官方文件 URL / 查閱日期；既有結構與待確認差異：
- 靜態資源策略：本地資源 / 外部資源 / 是否需 on-premise 支援
- Routes:
- Controller:
- FormRequest:
- Action/Service:
- Model/Migration:
- Policy / gate / guard / tenant context：
- 輸入、mass assignment、sort / filter allowlists：

## 任務拆解
1. 
2. 
3. 

## 風險與緩解
- 外部資源風險：若使用 CDN、gstatic、第三方字型/圖片/JS/CSS，列出 URL/網域、用途、CSP 需求與本地化替代方案。
- 風險：
- 緩解：

## 驗證方式
- [安全驗收矩陣](security-acceptance-matrix.md)：allowed / denied / cross-tenant / validation / 無副作用
- 測試命令：
- 預期結果：
- 已跑 / 失敗 / 未跑（原因）：

