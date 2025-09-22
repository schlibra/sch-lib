---
title: 密码工具
---
# 二维码工具
::: tip 该模块依赖[qrcode]
```bash
pip install sch-lib[qrcode]
```
:::
## 打印二维码
::: tip 打印二维码
`qrcode_print(_data: str, _border: int, _invert: bool) -> void`
:::
传入二维码包含数据，设置边框宽度（**默认为1**），和是否启用颜色反转（**默认为不启用**），并输出在这个二维码。
```python [qrcode.py]
from sch import qrcode_print

qrcode_print('https://sch-lib.schhz.cn', 1, True)
```
## 生成二维码
::: tip 生成二维码
`qrcode_image(_data: str, filename: str, _border: int) -> void`
:::
传入二维码包含数据，设置输出文件名，和边框宽度（**默认为1**），并保存到指定文件。
```python [qrcode.py]
from sch import qrcode_image

qrcode_image('https://sch-lib.schhz.cn', 'qrcode.png', 1)
```