# Comparison 系列封面

2026-11-24 用户认可双产品卡片方向，要求固定 comparison 博客的风格，并将 Goose / Codex CLI 和 YuE2 Studio / Music Studio 各适配三个尺寸。本规范仅用于两款应用、工具或服务的 comparison 封面，不替代教程、发布、活动等其他文章的视觉选择。

## 固定与可变部分

固定阅读顺序：Olares 官方标识 → 主标题 → 两个产品标识及名称。宽版和横版为左侧标题、右侧双卡片；方形版为上方标题、下方双卡片。两张卡片同尺寸、同材质、同光源，轻微错位，中间小号 `vs.` 表达比较，不靠大小或高低宣告胜负。

每篇替换：标题、产品名、官方 Logo；按主题选择背景色与卡片色调。可以改变背景画风和材质，但保持上述结构与视觉权重。柔光玻璃是当前基线；纸感、哑光等是允许探索的变体，并非已经获得认可的成图。不要因为文章换了主题就重新发明整套布局，也不要把所有文章统一成相同底色。

标题通常两行，Poppins Bold，深色字配浅色底。保留已确认标题；不自动加年份、营销副标题、眉题、按钮或胜负标记。产品名为卡片内独立标签；确有辨识需要时允许一行从属的模型/引擎名，例如 Music Studio 下的 ACE-Step。

标识必须来自应用官网、官方仓库或 Olares 官方应用清单。不要用示意波形冒充官方 Logo，也不要让模型重画标识。使用产品专属标识时优先于厂商通用标识，例如 Codex 专属图标。PNG 图标外围留白可用独立视口或蒙版隐藏，保留原素材及形状比例。

## 三种尺寸

用户只要一张或用于普通博客发布时默认做 1600 × 900 横版。1800 × 600 宽版不再是默认交付要求。明确要求“三个尺寸”且未另指定时采用下表。用户指定渠道尺寸优先。不要未经请求直接创建三个版本。

| 格式 | 尺寸 | 构图与起始参数 |
| --- | --- | --- |
| wide | 1800 × 600 | 左文右图；Logo 约 (82,70)，宽 190；标题基线 y=282，行距 100，字号 76–80；卡片 290，位置 (1030,133) 与 (1400,221) |
| landscape | 1600 × 900 | 保持左右阅读；Logo 约 (80,80)；标题基线 y=380，行距 96–100，字号 70–80；卡片 310，位置 (860,225) 与 (1220,405) |
| square | 1200 × 1200 | 上方品牌与标题，下方双卡片；Logo 约 (80,78)；标题基线 y=275，行距 100–105，字号 78–88；卡片 350，位置 (160,530) 与 (690,660) |

坐标与字号是这组已交付设计的起点，不是防溢出算法。按实际标题长度检查换行与背景亮边。两个 Logo 应按可见图形面积平衡大小，不能仅给不同留白的素材相同边长。导出后同时看完整画面与约 400 px 宽缩略图。

三种比例各有独立背景构图，不能拉伸宽图或给它上下加边。横版的背景细节集中在右半区；方形版将主要曲线下移，为上方标题留白。只改标题或产品 Logo 时复用背景；只改配色时以原背景为参考改色，保持轮廓与光源。

## 可复用资产与脚本

`assets/comparison/` 提供蓝绿和紫桃两组背景，每组包含 wide / landscape / square，另有两份可运行示例配置、官方应用图标及预览。它们是本系列模板资产，不是设计师历史样本或官网已发布头图。字体不内嵌。

```sh
python3 scripts/compose_comparison.py assets/comparison/agents.json output/agents --format wide landscape square
python3 scripts/compose_comparison.py assets/comparison/music.json output/music --format wide landscape square
```

脚本依赖同目录 `compose_svg.py`，仅使用 Python 标准库。它产出自包含 SVG，PNG 仍需按 [svg-production.md](svg-production.md) 使用实际 Poppins 字体渲染。不要将浏览器字体替代误认为目标效果。

新文章先复制示例配置和要用的素材到任务目录，再调整：

- `title`：逐行文字。
- `brand`、`backgrounds`、`products[].icon`：相对配置文件的素材路径。
- `ink`、`secondary`、`shadow`、`surface`、`products[].tint`：文字及卡片配色。
- `products`：恰好两项；`name` 为标签，`engine` 可选，`icon_fraction` 为标识边长与卡片边长之比。
- `products[].crop`：仅用于 PNG 等素材的视口裁切，包含 `viewbox`、原图尺寸和可选圆角；原图仍内嵌。
- `layouts`：按格式覆盖品牌位置、标题位置/行距/字号、卡片位置/尺寸或 vs. 位置；未覆盖时使用脚本预设。

背景、品牌、标题、每个产品的卡片/阴影/标识/名称、引擎标签和 vs. 均独立命名。背景和 PNG 标识仍是位图；卡片为矢量渐变、阴影为单独滤镜组。这不是实时背景模糊。未实际导入 Figma 就不要宣称原生效果或字体完全兼容。

保留源素材、提示词、配置与组装代码，交付每种尺寸的 PNG 和 SVG。技能内示例的应用图标是读取当日资产，后续涉及该应用时核对是否更新。替换应用不能保留旧名称、旧图标或示例标题。

## 背景提示词

基线：高明度的柔光工作室，轻盈半透明宽丝带、克制反射和接触光；无字、无 Logo、无卡片，文字区低细节。蓝绿版采用冰蓝与薄荷，紫桃版采用浅紫与暖桃；这些是编辑设计色调，未宣称精确采用官方标准色。

改比例时使用对应已认可背景作为参考，明确目标比例、标题留白、未来卡片的位置。横版右侧放丝带；方形上方 45% 安静，主要丝带集中在下半部和右缘。无唱片、音符、漂浮圆片、粒子或额外图标。只改配色时要求保持曲线、光照、留白和裁切边界。

## 示例图标来源

- Goose：https://raw.githubusercontent.com/block/goose/main/documentation/static/img/goose.svg
- Codex：https://developers.openai.com/images/codex/icons/app-homepage-logo.svg
- YuE2 Studio：https://github.com/beclab/apps/blob/main/yue2studio/OlaresManifest.yaml ，图标 https://cdn.olares.com/images/2026/11/820c3ea1b560cc4e73454261ad182c1d.png
- Music Studio：https://github.com/beclab/apps/blob/main/acestepmusicv3/OlaresManifest.yaml ，图标 https://app.cdn.olares.com/appstore/acestep/icon2.png

读取日期 2026-11-24。第三方标识的权利归各自所有者；示例不表示合作或背书。
