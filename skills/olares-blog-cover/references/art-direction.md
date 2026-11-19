# 视觉参考与已验证的偏好

设计师提供的 Figma 历史头图研究见 [figma-cover-study.md](figma-cover-study.md)（2026-11-02，10 个主题、12 张画板）。新设计参考其构图、材质与比例适配；下文保留官网来源及各次用户反馈，两者不要混为同一种证据。

## 2026-10-30 的参考记录

在官网博客第 1–4 页比较了 18 张已发布封面。入口为 [博客首页](https://www.olares.com/blog/)、[第 2 页](https://www.olares.com/blog/page/2/)、[第 3 页](https://www.olares.com/blog/page/3/)、[第 4 页](https://www.olares.com/blog/page/4/)。这是当时的样本，不代表完整品牌规范。

复核时可优先查看这些具体图片：

- [Credentials overview](https://www.olares.com/blog/wp-content/uploads/2026/10/olares-credentials-overview.png)：解释型文章参考。
- [Olares CLI and AI agents](https://www.olares.com/blog/wp-content/uploads/2026/09/olares-cli-ai-agents-explained.jpg)：概念关系文章参考。
- [Ticket support app](https://www.olares.com/blog/wp-content/uploads/2026/09/introducing-ticket-support-app.jpg)：产品功能文章参考。
- [FlowStudio image to video](https://www.olares.com/blog/wp-content/uploads/2026/10/flowstudio-image-to-video-1.png)：应用教程参考。
- [Local AI hardware benchmarking](https://www.olares.com/blog/wp-content/uploads/2025/11/Olares-Blog-Local-AI-Hardware-Performance-Benchmarking.png)：硬件与性能内容参考。

比较的是图文层级、配色、留白与质感。教程、技术解释、活动报道、产品发布不一定采用同一视觉语法；不要把活动照片直接当作所有博客封面的模板。

## 本次模型文件教程的迭代经验

文章最终标题：**How to Choose Model Files for Olares**。主题是理解模型来源并选择适合 Olares 的模型文件；头图没有副标题。

用户拒绝了两种方向：

- 重金属、玻璃高光、硬件底座式的 3D 模型卡匣，气质与文章不合。
- 过度简化的扁平文件夹，加上三行完整长标题，画面和标题都不理想。

获得认可的方向：浅色背景，轻盈的纸张叠层与蓝绿纸带，Hugging Face / Ollama 官方标识作为识别点，清楚的大标题与充足留白。随后修改标题时保留了这套主视觉。

这些反馈意味着减少沉重材质与装饰，保留适当层次；**不意味着永远禁止 3D、永远必须用纸张、或所有文章都使用蓝绿色**。新主题应选择适合内容的隐喻。

最终示例的排版参数可作起点，不作硬规范：

- 1800 × 600；Olares Logo 左上，约 190 × 44.84。
- 英文标题 Poppins 700，字号 76；两行同级：`How to Choose` / `Model Files for Olares`。
- 左侧文字、右侧主视觉；深蓝黑文字，浅灰蓝与薄荷绿背景。

## 2026-10-30：Unsloth 微调教程的迭代经验

文章介绍在 Olares 上用 Unsloth 微调本地工单分类器。头图标题为 **Fine-Tune a Local Classifier with Unsloth**，没有营销副标题。

首版使用浅蓝绿背景、可调滑块模型块、输入纸片和分类纸堆。用户反馈“这个图有点抽象”，并询问是否使用了 Design Taste。问题是主视觉仅能表示通用的调整和分类，缺少能辨认 Unsloth 训练任务的内容；这不等于否定配色或整体排版。

修订版保留标题、字体、Logo 位置和浅蓝绿配色，将右侧换成文章中真实的 Unsloth 训练完成界面，在前景加入具体工单及对应标签：

- 输入：`My transfer still says pending three days later.`
- 输出：`{"intent":"pending_transfer"}`

这是一组来自正文的示意输入/预期输出，不是声称重新执行模型得到的结果。截图保留实际训练状态与曲线，没有让模型重画界面。

用户对修订版反馈：“可以 这个我也能接受”。将它记为**获认可的另一种方案**，而非所有头图必须采用的唯一模板。

用户随后特别认可了配色与应用品牌的呼应，指出 Unsloth 的绿色被用于背景方向。本例实际使用浅蓝绿底色、绿色输出块，与真实界面中的绿色 Unsloth 标识和训练进度形成呼应；这些颜色没有被核验为 Unsloth 的官方标准色值。可迁移的偏好是：以文章主角的品牌色作为配色依据，并调整明度和饱和度来服务背景与视觉重点，同时保留 Olares 的品牌识别。不是所有应用都继续使用绿色。

公开分发包不附带本地生成稿缩略图。需要视觉复核时，使用当次任务提供的原稿或已发布的官网图片。

可迁移的判断：教程和实验文章优先检查是否已有可用的真实界面与具体输入/输出；选择插画时，也要让工具或任务有可识别的线索。不要仅凭“大标题 + 浅色 3D”判断设计已完成。对用户认可的布局保持连续性，只修正反馈针对的问题。

本例参数仅供参考：1800 × 600；标题 Poppins 700 / 68 px，两行；工单 Poppins 500，真实 JSON 使用等宽字体；界面位图内嵌，示例文字独立可编辑。

## 2026-10-30：Hermes Agent / Hindsight 记忆主题的迭代经验

文章介绍在 Olares 上自托管 Hindsight，为 Hermes Agent 提供持久记忆；头图标题为 **Hermes Memory / with Hindsight**。需要表达的关系是：从保留的经历中唤回与当下相关的信息，而不只是泛化的“连接”。

本次用户反馈与方向状态：

- 纸片、存储卡片等通用隐喻被认为抽象；改成具体流程并没有解决画风不合的问题。用户指出迭代在走极端。
- 密集神经节点组成的大脑让用户感到害怕和密集不适；平滑褶皱版本被联想到肠道。降低节点密度并不能自动消除解剖感。
- 用户认可“记忆星图”的想法，但否定了当时的成图；随后尝试的浅色棱角马赛克大脑也未获认可。不能将这些尝试记作已接受的视觉基线。
- 用户提出“深色背景，一片星星中有几个连成线”。初版星空中向右上方延伸的折线更像增长曲线，只表现了连接，没有充分表达唤回记忆。
- 用户同意改为局部、不规则、微微亮起的小星座，并提出深空过黑、参考 Hermes Agent 的颜色。随后交付了较明亮的钴蓝背景与局部星座版本；截至本记录，用户未明确评价这张新成图，不记为最终认可稿。

本次色彩参考为 [Hermes Agent 官网](https://hermes-agent.nousresearch.com/)，实际查看了页面中的鲜明电蓝色。封面以较柔和的钴蓝色呼应，保留白色标题与 Olares Logo；没有核验为官方标准色值。

本次视觉映射：散落星点代表保留的经历，局部连线及亮起的星点代表其中被重新关联、唤回的记忆。它是本文的概念插画方向，不是 Hindsight 的实际数据结构示意，也不意味着以后所有记忆主题都用星空。

可迁移的方法是保留已认可的部分、检查图形是否产生其他更强的含义，并在首次生成前参考主角产品的配色。对解剖感、密集节点的反感及星空方向的认可，属于这次任务的偏好；后续仍以用户当次要求为准。

## 2026-10-31：Qwen / Strata 的纯图形背景方向

文章标题为 **Run Qwen3.8-Flash-Next on a 24GB GPU with Strata**。用户提供 Home Assistant 的多张博客封面作为参考，最终选定浅薄荷色几何背景，并认可去掉 Strata 标识、只保留 Olares 品牌与标题的方向。随后标题由左侧三行窄排改为两行，完整模型名横向展开到画面中部，规格与工具名置于从属行，用户认可这次调整。

可沿用的是设计思路：

- 以明确的标题交代文章主题，图形背景承担视觉氛围与构图，不要求每篇都找到一个具象隐喻、硬件设备或第三方 Logo 作为主角。
- 用文字尺度、粗细、横向跨度和图形疏密组织整张画面，避免把标题机械地限制在左半边。背景可以延伸到文字后方，但需要保证阅读对比。
- 品牌连续性可以来自 Olares 标识、排版质量与整体气质，不依赖相同装饰或固定配色。

用户明确要求：“不用一模一样复用，但是那种思路可以再次沿用”。因此不把本次薄荷绿、紫色、几何拼接、坐标或字号固化为模板；后续按文章重新设计形状、节奏、颜色和标题布局。纯图形背景是与概念插画、真实界面并列的可选方向，不替代所有教程的截图需求。

本次不希望 24GB 成为焦点、不使用真实主机，以及不再沿用此前 Hugging Face / Ollama 的纸张叠层风格，属于本轮明确反馈，不推广为对所有博客的禁令。Home Assistant 参考来自用户提供的图片，不是 Olares 官网历史样本。

## 品牌资产来源

`assets/olares-logo-black.svg` 来自官方 BrandKit 的 `SVG/Standard/logo_black.svg`，原始 viewBox 为 `0 0 1000 236`。保留原始路径和比例。此资产是 Logo，不是历史头图参考。

本次第三方素材来源：

- Hugging Face：https://huggingface.co/front/assets/huggingface_logo-noborder.svg
- Ollama：https://ollama.com/public/ollama-nav.png

使用时核对链接及当前品牌资产；不要从本次实例推断它们必须出现在其他文章封面里。
