# Skill 01 — Static Assets & External Resources

## 目的
確保靜態資源在不同部署環境中可控、可離線化，避免因外部 CDN 或第三方資源造成 on-premise、資安、法遵或可用性風險。

## 核心原則
1. **靜態資源優先使用相對路徑**：專案內的圖片、字型、CSS、JavaScript、icon、manifest、下載檔案等，應盡可能透過相對路徑或 Laravel/Vite 的本地 asset pipeline 引用。
2. **避免不必要的外部資源依賴**：不要為了方便直接引用外部 CDN asset；若可由 npm、Composer、Vite build、`public/` 或 `resources/` 管理，應優先放在本地。
3. **外部 CDN asset 必須先澄清部署需求**：若需求或範例中使用 `fonts.gstatic.com`、`fonts.googleapis.com`、cdnjs、jsDelivr、unpkg、第三方圖片/字型/腳本等 URL，必須詢問使用者是否有 on-premise、離線環境、內網部署、CSP、資料主權或不能連外的限制。
4. **若有 on-premise 需求，避免直接連外**：確認有 on-premise 或不能依賴外網時，應改成本地化資源，或提供把外部資源複製、授權確認、版本鎖定並納入專案 build/deploy 流程的方案。

## 實作規範
- Blade / Livewire / Inertia / Vue / React 內引用本地資源時，優先使用相對路徑、`asset()`、Vite `@vite()`、npm package 或專案既有 asset helper。
- 外部字型應優先改為 self-hosted font files，並檢查授權、格式（如 `woff2`）與 fallback font stack。
- 外部 JavaScript/CSS library 應優先透過 package manager 安裝並由 Vite 打包；不得只貼 CDN `<script>` 或 `<link>` 後就交付。
- 外部圖片、icon、logo、map tile、captcha、analytics、embed widget 等若必須連外，需在實作計畫與 PR 說明中標示原因、網域、用途、風險與替代方案。
- 若無法立即本地化，至少要提供設定開關或環境變數，讓部署者可在 on-premise 環境禁用或替換外部資源。

## 需求澄清問題
當發現會使用外部靜態資源時，先問：

1. 這個系統是否需要支援 on-premise、內網、離線或不能連外的部署？
2. 是否有 CSP、資安審查、資料主權或第三方網域白名單限制？
3. 外部資源是否可以複製到本地並由專案 build/deploy 流程發布？

## 輸出要求
- 實作計畫需列出「靜態資源策略」：本地資源、外部資源、是否需 on-premise 支援。
- PR checklist 需確認沒有未說明的外部 CDN asset。
- 若保留外部資源，需記錄 URL/網域、用途、失效風險、CSP 需求與 on-premise 替代方案。

## 反模式
- 直接貼上 Google Fonts / gstatic / CDN script，未詢問部署限制。
- 可由 npm/Vite 打包的 library 卻使用未鎖版本的 CDN URL。
- 使用絕對 URL 指向同站靜態資源，導致 staging、子目錄部署或 on-premise 環境失效。
- PR 中新增第三方資源但沒有說明用途、授權與替代方案。
