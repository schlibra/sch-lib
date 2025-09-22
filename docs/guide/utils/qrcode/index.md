---
title: 密码工具
---
# 二维码工具
## 打印二维码
::: tip 打印二维码
`qrcode_print(_data: str, _border: int, _invert: bool) -> void`
:::
传入二维码包含数据，设置宽度（**默认为1**），和是否启用颜色反转（默认为**不启用**），并输出在这个二维码。
```python
from sch.util import qrcode_print

qrcode_print('https://xtiantech.cn',1,True)
```
## 生成二维码图片

::: tip 生成二维码图片
`qrcode_print(_data: str, _border: int, _invert: bool) -> void`
:::
传入二维码包含数据，设置宽度（**默认为1**），和是否启用颜色反转（默认为**不启用**），并输出在这个二维码。
```python
from sch.util import qrcode_print

qrcode_print('https://xtiantech.cn',1,True)
```

