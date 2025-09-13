---
title: Markdown转换
---

# Markdown转换
用于快速将Markdown文本与HTML进行相互转换。
::: tip 该模块依赖[markdown]
```bash
pip install sch-lib[markdown]
```
:::
## 1. Markdown转HTML
```python
from sch import markdown_to_html

html = markdown_to_html("**Hello, World!**")
print(html)
```
::: details 输出
```html
<p><strong>Hello, World!</strong></p>
```
:::

## 2. HTML转Markdown
```python
from sch import html_to_markdown

markdown = html_to_markdown("<p><strong>Hello, World!</strong></p>")
print(markdown)
```
::: details 输出
```markdown
**Hello, World!**
```