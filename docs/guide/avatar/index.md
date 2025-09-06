---
title: 头像生成
---
# 头像生成
生成Github风格哈希头像，通过输入文本的哈希值，可以生成不同的头像。
::: tip 方法
`generate_avatar(code: str=None, algo: Algo=Algo.SHA512, filename: str=None, output_dir: str=None, _return=False)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `code` | `str` | 输入的文本 |
| `algo` | `Algo` | 哈希算法，默认使用`SHA512`，可选`MD5`、`SHA1`、`SHA224`、`SHA256`、`SHA384`、`SHA512` |
| `filename` | `str` | 输出文件名，默认使用{output_dir}/{algo.value}/{source}.png，可自定义；自定义时，不需要指定后缀名 |
| `output_dir` | `str` | 输出目录，默认使用output，可自定义 |
```python {4}
from sch.avatar import generate_avatar
from sch.avatar.enum import Algo

generate_avatar('schlibra', Algo.SHA512, 'avatar', '.')
```
这将会生成一个头像并存储在当前目录下的`avatar.png`文件中。
![avatar.png](avatar.png)