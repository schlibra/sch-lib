---
title: 密码工具
---
# 密码工具
## 密码隐藏
::: tip 密码隐藏
`password_hide(_password: str) -> str`
:::
传入密码字符串，隐藏密码中间的部分字符，仅保留前后两位字符，中间用星号代替。
```python
from sch.util import password_hide

print(password_hide('123456'))
```
::: details 输出
`1****6`
:::