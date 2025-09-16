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

## MD5哈希生成
::: tip MD5哈希生成
`md5(_password: str) -> str`
:::
```python
from sch.util import md5

print(md5("hello world"))
```
::: details 输出
`5eb63bbbe01eeed093cb22bb8f5acdc0`
:::

## 生成随机密码
::: tip 生成随机密码
`generate_password(_length: int, _strong_password: bool) -> str`
:::

这个函数用于生成随机密码，提供了两种强度选项，特性：生成指定长度的随机密码默认长度为 `8`
。基于 `UUID` 算法生成，具备良好的随机性。
```python
from sch.util import generate_password
#第一个参数是长度，第二个参数是是否启用加强密码
print(generate_password(10, True))
```
::: details 可能输出
`5eb63bbbe01eeed093cb22bb8f5acdc0`
:::

## 生成UUID
:: tip 生成UUID
`uuid() -> str`
:::
```python
from sch.util import uuid
print(uuid())
```

## 凯撒密码加密（未经严格测试，推荐搭配base64）
:: tip 凯撒密码加密
`caesar(_text: str, _key: int) -> str`
:::
**_注意，仅支持大小写英文字母数字和=/_**
```python
from sch.util import caesar
print(caesar("aaaAAA123/", 2))
```
::: details 输出
`cccCCC345b`
:::
