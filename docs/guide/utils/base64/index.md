---
title: Base64转换
---
# Base64转换
由于Python自带的base64需要转换时要写的代码比较长，如果经常需要转换，可以写一个函数来简化操作。
## Base64编码
```python
from sch.util.base64 import base64_encode

text = base64_encode('hello world')
print(text)
```
::: details 输出
`aGVsbG8gd29ybGQ=`
:::
## Base64解码
```python
from sch.util.base64 import base64_decode

text = base64_decode('aGVsbG8gd29ybGQ=')
print(text)
```
::: details 输出
`hello world`
:::