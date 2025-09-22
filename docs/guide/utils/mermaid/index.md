---
title: Mermaid
---

# Mermaid
Mermaid是一个基于Javascript的流程图绘制工具，可以将流程图语法直接写入Markdown文档中，并通过渲染生成流程图。
::: tip 该模块依赖[request]
```bash
pip install sch-lib[request]
```
:::
## 渲染流程图
::: tip 渲染流程图
`render_mermaid(graph: str, save_path: str) -> void`
::: 
渲染流程图的函数，参数`graph`为流程图的语法，`save_path`为保存路径。
```python [mermaid.py]
from sch import render_mermaid

graph = '''
graph LR
A[开始] --> B[步骤1]
B --> C[步骤2]
C --> D[步骤3]
D --> E[结束]
'''

render_mermaid(graph, 'flow.png')
```