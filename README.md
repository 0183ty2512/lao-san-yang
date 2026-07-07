# 大气科学学习笔记

> 一份以 **Obsidian + Markdown + LaTeX** 为核心的气象学复习资料库，涵盖动力气象、大气物理学、天气学分析原理等核心课程。

📂 在线浏览：[github.com/0183ty2512/lao-san-yang](https://github.com/0183ty2512/lao-san-yang)

---

## 目录结构

```
.
├── 动力气象/              # 动力气象学笔记+习题集
│   ├── 大气运动的基本方程组/
│   ├── 大气中的基本波动/
│   ├── 大气行星边界层/
│   ├── 大气能量学/
│   ├── 不稳定理论/
│   ├── 低纬度大气动力学/
│   └── 习题集/            # 第1-7章习题与解答
│
├── 大气物理学/            # 大气物理学知识点
│
├── 天气学_GPT整合版/      # GPT辅助整理的天气学笔记
│
├── 天气学分析原理/         # 天气学原理+天气图分析
│
├── 流体力学/              # 流体力学I 考点+例题（公众号排版版）
│
├── 往年试题分析/           # 历年考题解析
├── 模拟试题/              # 模拟题
└── 补充内容/              # 其他补充材料
```

---

## 快速开始

### 1. 克隆到本地

```bash
git clone https://github.com/0183ty2512/lao-san-yang.git
```

### 2. 用 Obsidian 打开

1. 打开 **Obsidian**
2. 点击左下角 **"打开其他仓库"**（Open folder as vault）
3. 选择克隆下来的 `lao-san-yang` 文件夹
4. Obsidian 会自动识别 `.md` 文件、`[[双向链接]]`、标签和图谱

> 💡 建议安装 Obsidian 社区插件：
> - **LaTeX Suite** — 快速输入数学公式片段
> - **Pandoc Plugin** — 一键导出 PDF/Word
> - **Tag Wrangler** — 管理标签
> - **Graph View** — 可视化知识图谱

---

## Markdown 写作规范

本项目统一使用以下规范，确保 Obsidian、GitHub、Pandoc 均能正确渲染。

### 标题层级

```markdown
# 一级标题（文章标题）
## 二级标题（大节）
### 三级标题（小节）
```

### 数学公式（LaTeX）

| 场景 | 写法 | 示例 |
|:--|:--|:--|
| 行内公式 | `$...$` | `$u = \omega y$` → $u = \omega y$ |
| 独立公式 | `$$...$$` | `$$\frac{p}{\rho} + \frac{u^2}{2} = C$$` |
| 多行对齐 | `aligned` 环境 | 见下方示例 |

**多行公式示例：**

```latex
$$
\begin{aligned}
a_x &= \frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} \\
    &= (6x-4y) + (6x-4y)t \cdot 6t + (9x-6y)t \cdot (-4t)
\end{aligned}
$$
```

> ⚠️ **常见错误**：不要在行内公式用 `$$...$$`（会导致公式独占一行，破坏段落），行内公式一律用 `$...$`。

### 常用 LaTeX 符号速查

| 符号 | 代码 | 含义 |
|:--|:--|:--|
| `\nabla` | $\nabla$ | 梯度/散度算子 |
| `\partial` | $\partial$ | 偏导数 |
| `\mathbf{u}` | $\mathbf{u}$ | 向量 |
| `\cdot` | $\cdot$ | 点乘 |
| `\times` | $\times$ | 叉乘 |
| `\frac{a}{b}` | $\frac{a}{b}$ | 分数 |
| `\dfrac{a}{b}` | $\dfrac{a}{b}$ | 大分数（行间用） |
| `\oint` | $\oint$ | 环路积分 |
| `\iint` | $\iint$ | 面积分 |
| `\sum` | $\sum$ | 求和 |
| `\int` | $\int$ | 积分 |
| `\infty` | $\infty$ | 无穷 |
| `\partial` | $\partial$ | 偏导 |
| `\text{...}` | $\text{abc}$ | 公式中插入普通文字 |
| `\quad` | 空格 | 公式内空格 |

### Obsidian 双向链接

使用 `[[页面名]]` 链接到同一仓库内的其他笔记：

```markdown
[[伯努利方程]]
[[N-S方程]]
[[斯托克斯公式]]
```

- Obsidian 中点击 `[[链接]]` 会跳转到对应笔记
- GitHub 上渲染为可点击链接（如果对应 .md 文件存在）
- 导出 PDF 时建议用 Pandoc 插件或转为纯文本引用

### 标签

在文件顶部 YAML front matter 中声明标签：

```yaml
---
tags:
  - 流体力学
  - 考点
  - 例题
---
```

Obsidian 会自动按标签聚合，方便按主题检索。

---

## 导出 PDF

### 方法一：Obsidian 内置（最简单）

打开笔记 → 右上角 `...` → **导出 PDF**。  
适用于单文件，公式可正常渲染。

### 方法二：Pandoc（推荐，适合批量）

```bash
# 安装 pandoc + xelatex（如已安装 MiKTeX 或 TeX Live）
pandoc 流体力学I-考点与例题-公众号版.md \
  -o 流体力学I-考点与例题.pdf \
  --pdf-engine=xelatex \
  -V CJKmainfont="SimSun" \
  --mathjax
```

### 方法三：Typora

用 **Typora** 打开 `.md` 文件 → 文件 → 导出 → PDF。Typora 内置 LaTeX 渲染，所见即所得。

---

## 发布到微信公众号

本项目包含数学公式文章，微信原生编辑器不支持 LaTeX，采用**长截图方案**：

1. **下载公式 SVG**：调用 codecogs API，将每个 `$...$` / `$$...$$` 渲染为 SVG 图片
2. **生成 HTML**：将 Markdown 转为带内联 SVG 的 HTML 页面
3. **Playwright 截图**：用 Chromium 渲染 HTML 为整页 PNG 长图（750×2x dpi）
4. **上传微信**：通过公众号 API 上传截图、封面，创建草稿

详细脚本见 [`wechat_formula_publish.py`](https://github.com/0183ty2512/lao-san-yang)（在配套的公众号发布工具中）。

---

## 常见问题

<details>
<summary><b>Q: GitHub 上公式显示为原始代码？</b></summary>

GitHub 原生不支持 `$...$` 渲染。建议：
- 本地用 Obsidian / Typora 查看
- 或安装浏览器插件 **"MathJax 3 Plugin for GitHub"**
</details>

<details>
<summary><b>Q: Pandoc 导出 PDF 中文乱码？</b></summary>

需要指定中文字体：
```bash
pandoc file.md -o file.pdf --pdf-engine=xelatex -V CJKmainfont="SimSun"
```
确保系统安装了对应字体。
</details>

<details>
<summary><b>Q: Obsidian 打开后链接全是灰色？</b></summary>

正常现象——灰色表示链接指向的笔记暂未创建。只要对应 `.md` 文件存在仓库中，链接就会变蓝。如果确认文件存在但仍是灰色，检查文件名是否完全一致（区分大小写）。
</details>

---

## 贡献

欢迎提交 Issue 或 PR：
- 发现公式错误 → 提交 Issue 标注"勘误"
- 补充新笔记 → Fork 后 PR
- 优化排版 → 直接在对应的 `.md` 文件中修改

---

## 许可

个人学习笔记，仅供学习交流使用。如需转载，请注明出处。
