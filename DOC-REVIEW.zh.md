# medux-api-examples 文档规范评审

评审对象：`medux-api-examples` 仓库
参照基准：<https://medux.io/api-reference/> 与 <https://medux.io/tutorials/>
评审日期：2026-07-21

## 一、总体结论

仓库整体质量高、结构规范：68 个 API 端点与官方 API Reference 一一对应（已用
`examples.json` / `api-reference.json` / 校验脚本核对，数量一致），每个端点都提供
`README.md + curl.sh + example.py + example.mjs + request.json + reference.json`
六件套，README 分节（Endpoint / Authentication / Preconditions / Request /
Response / Official sample / MCP alternative / Related APIs / Source of truth）
覆盖了官方参考页的全部板块，并有 CI（`.github/workflows/validate.yml`）+
`validate_examples.py` 做结构、语法、密钥、死链校验。这套"以生成器为准、快照可复核"
的做法是规范的。

但对照官方参考站点后，仍存在若干**应当说明而未说明**、以及**格式不规范**的问题。
下面区分"已修复"和"建议后续处理"两类列出。

## 二、发现的问题与差距（均已在仓库中核实）

### 1. 响应码（`code`）说明不完整且格式不统一 — 最主要问题

- 68 个端点中有 **56 个**在 `code` 的 `Options` 里列出了枚举值，却在"含义表"中
  **缺少对应行**（如 `1406`、`1407`、`1408`、`1409`、`1410`），读者只看到数字、
  看不到含义。
- 全仓库对响应码含义的说明**没有任何一处是完整的**：跨端点合并后也只覆盖 11 个码，
  而 `1406/1407/1408` 在整个官方快照里**都没有任何含义说明**（确属官方缺失）。
- **2 个端点**（`generate/create-image-to-video`、`generate/create-text-to-video`）
  的 `code` 描述是从参考页泄漏出来的原始文本，直接渲染成了
  `response code enums:<br>.. 0: ok<br>....  1401 ~ 1499 是 media<br>...`——
  夹带 `..`/`....` 圆点符和一句未翻译的中文"是 media"，非常不规范。
- 另有 1 处（`infra/list-assets` 的 `status` 查询参数）同样泄漏了原始
  `. assethpb.Status:<br>... enums:<br>..... ACTIVE` 这类 protobuf 文本。

### 2. 缺少面向新用户的总体说明（onboarding 缺口）

对照姊妹仓库 `medux-mcp-examples`（它有 `docs/concepts.md` 等），本仓库缺少统一的
概念说明，导致以下关键信息只散落在各端点、或根本没讲：

- **文件 vs 资产（file_id / asset_id）** 的区别与获取方式；
- **上传流程**（先 Create Upload URL，再上传，再拿 file_id 调用）；
- **异步任务生命周期**：大多数 POST 只返回 `data.task`，必须轮询对应
  Get *Task 端点，HTTP 200 不代表处理完成；
- **积分 / 付费计划**（`insufficient credits` / `paid plan required`）；
- **分页**（`cursor` / `limit` / `next_cursor`）。

### 3. 环境变量 `MEDUX_API_BASE_URL` 未被文档说明

`example.py` 与 `example.mjs` 都读取了 `MEDUX_API_BASE_URL`，但根 README 和端点
README 从未提及该变量，属于"代码用到、文档缺失"。

### 4. `.env.example` 缺失，且与既有约定矛盾

- `.gitignore` 里有 `!.env.example`（保留例外），`CONTRIBUTING.md` 要求新增代码
  必须"include an `.env.example` containing placeholders only"，但仓库里**没有任何
  `.env.example`**，前后矛盾。

### 5. 缺少 LICENSE

姊妹仓库 `medux-mcp-examples` 带 MIT LICENSE，本仓库 README/CONTRIBUTING 明示欢迎
PR、可 clone 使用，却**没有 LICENSE 文件**，开源合规性缺口。

### 6. 根 README 缺少 Prerequisites

未说明所需的 Python / Node.js 版本（代码要求 Node ≥18、`requests`），新用户无从
判断运行环境。

### 7. 示例数据自相矛盾（`get-started/create-upload-url`）

`request.json` / `curl.sh` 使用 `{"extension":"png","media_type":"VIDEO"}`——扩展名
是图片 png，媒体类型却是 VIDEO，而该端点参考页明确"media_type 用于校验 extension"，
此样例很可能被服务端判为非法输入。此数据来自官方样例，属**内容层面**问题。

### 8. 次要：Python 示例未显式设置 `Content-Type`

`example.py` 依赖 `requests` 的 `json=` 自动加头，功能正确，但与 `example.mjs`、
`curl.sh` 显式声明 `Content-Type: application/json` 的风格不一致。

## 三、本次已做的修改（仅改手写/生成器，未手工编辑生成的示例）

遵循"示例由脚本生成、不手工编辑"的约定，改动集中在**手写文档**与**生成器**：

新增手写文件：

- `LICENSE`（MIT，与姊妹仓库一致）。
- `.env.example`（补齐 §4 缺口，含 `MEDUX_API_KEY` / `MEDUX_API_BASE_URL` / 占位符）。
- `docs/concepts.md`（补 §2：文件与资产、上传流程、异步任务轮询、积分、分页）。
- `docs/error-codes.md`（补 §1：统一、完整的响应码总表，并显式标注 `1406/1407/1408`
  官方未公开含义、`1401–1499` 为 media 区间，给出重试/不可重试指引）。
- `docs/authentication.md`（补 §3/§6：前置条件、API Key、环境变量表、运行方式）。

更新手写文件：

- `CONTRIBUTING.md`：修正 `.env.example` 矛盾，补前置条件，明确"生成 vs 手写"边界，
  链接新文档。

修改生成器 `scripts/generate_examples.py`（再重新生成，从而统一修复全部 68 个示例）：

- 新增 `CODE_MEANINGS` 权威码表与 `code_details()`：把每个端点的 `code` 单元格渲染成
  **统一、完整**的含义列表，未公开的码显式标注为"Reserved media-domain error"，并链接
  `docs/error-codes.md`——修复 §1 的不完整与两处泄漏。
- 新增 `MALFORMED_DESC_RE`：检测并清洗任意字段里泄漏的 `..`/`enums:`/`xxxhpb.` 原始
  文本（修复 `list-assets` 的 `status` 字段），改用规范描述 + Options 行。
- 根 README 增加 `## Prerequisites` 与 `## Documentation` 两节，并说明
  `MEDUX_API_BASE_URL`、`.env.example` 用法。

更新校验器 `scripts/validate_examples.py`：强制要求 `LICENSE`、`.env.example`、
`docs/*.md` 存在，且根 README 含 Prerequisites / Documentation 两节，防止回退。

验证：`python3 scripts/generate_examples.py && python3 scripts/validate_examples.py`
输出 `Validated 68 API examples`；全仓库已无 `是 media` / 泄漏圆点 / proto 文本。
`git diff` 确认仅改动 README（生成物）、生成器、校验器、CONTRIBUTING 及新增文件，
`example.py/.mjs/curl.sh/request.json/reference.json` 未被改动。

## 四、建议后续处理（本次未自动改，多属需上游确认的内容问题）

1. **`1406/1407/1408` 的含义**：官方快照本身缺失，建议在 API Reference 中补全后，
   再更新 `CODE_MEANINGS` 与 `docs/error-codes.md`。
2. **`create-upload-url` 样例矛盾**（§7）：建议把官方样例改为
   `{"extension":"png","media_type":"IMAGE"}`（或 mp4+VIDEO）。因该数据源自
   `api-reference.json` 快照，宜在上游/快照层修正后重新生成，而非手改生成物。
3. **Python 显式 `Content-Type`**（§8）：可在生成器 `render_python` 里为带 body 的
   请求补 `"Content-Type": "application/json"`，与 JS/curl 保持一致。
4. 可考虑在生成器里为姊妹仓库 `medux-mcp-examples` 也补一份 LICENSE / 概念文档的
   交叉链接，保持两仓库体验一致。
