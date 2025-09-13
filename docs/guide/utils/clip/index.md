---
title: 剪切板
---

# 剪切板
用于在代码中快速操作剪切板。
::: tip 该模块依赖[clip]
```bash
pip install sch-lib[clip]
```
:::
## 复制文本
```python
from sch import copy_text

copy_text("Hello, world!")
```

## 粘贴文本
```python
from sch import paste_text

text = paste_text()
print(text)
```
::: details 输出
`Hello, world!`