# WORKFLOW — Laravel Skills 維護流程

> 目的：規範這個 skills repository 後續每次變更該怎麼調整，確保內容一致、可追蹤、可迭代。

## 1) 何時要更新

以下任一情況都必須更新文件：

1. 新增 skill（例如新增 Inertia、Queue、DDD 等主題）
2. 調整既有 skill 的步驟、輸出、命名規則
3. 新增或修改模板（`templates/*`）
4. 語系策略、fallback 或 tenant 覆蓋規則調整
5. Laravel / Livewire 版本升級造成最佳實務調整

## 2) 每次變更的固定步驟（SOP）

1. **先更新 `SKILLS_INDEX.md`**
   - 新增/刪除/改名 skill 時，先改索引表。
   - 確保「何時使用」「主要輸出」描述同步。

2. **再更新對應 skill 文件**
   - 只改有影響的章節（目的、步驟、輸出、反模式）。
   - 若是 breaking change，加入「升級提醒」。

3. **同步更新 `README.md`**
   - 若新增主題（如 Livewire/Queue），要更新「你會得到什麼」與「快速使用方式」。
   - 若流程改動，更新推薦流程描述。

4. **檢查模板是否需同步**
   - 若 skill 新增欄位或輸出格式，模板必須補齊。

5. **更新本檔 `WORKFLOW.md`（必要時）**
   - 若你改了維護規範本身，必須在 PR 說明清楚原因。

## 3) PR 最低要求

每次 PR 至少包含：

- 變更摘要（改了哪些 skill / 模板）
- 影響範圍（誰會受影響、是否 breaking）
- 使用方式差異（Before/After）
- 若有流程變更：附一段新流程示例

## 4) 版本與變更紀錄建議

建議使用下列方式維護版本節奏：

- `major`：大幅重構 skill 架構或命名
- `minor`：新增 skill 或新增模板
- `patch`：文字修正、範例微調、錯字修復

可在 PR 標題加前綴：
- `[major] ...`
- `[minor] ...`
- `[patch] ...`

## 5) 變更自我檢查清單

- [ ] `README.md` 是否反映最新 skill 組成？
- [ ] `SKILLS_INDEX.md` 是否與實際檔案一致？
- [ ] 新增 skill 是否有明確「目的 / 步驟 / 輸出」？
- [ ] i18n 是否提供 short/long/abbr 與 fallback 規則？
- [ ] 模板是否可直接複製使用？
- [ ] 是否避免重複與互相矛盾的規範？

## 6) 推薦提交順序

1. `SKILLS_INDEX.md`
2. 目標 skill 文件
3. `templates/*`
4. `README.md`
5. `WORKFLOW.md`

