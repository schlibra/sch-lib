---
title: IP计算
---
# IP计算
可将不同表示方式的IPv4地址进行相互转换
## 加载IP
### 常规IP
::: tip 常规IP
`from_ip(ip_str)`
:::
```python [from_ip.py]
from sch import IP

ip = IP.from_ip('192.168.1.1')
print(ip)
```
::: details 输出
```
IP Address: 192.168.1.1
IP Digits: 3232235777
IP Hex: C0A80101
IP Binary: 11000000101010000000000100000001
```
:::
### 数字类型IP
::: tip 数字类型IP
`from_digits(ip_int)`
:::
```python [from_digits.py]
from sch import IP

ip = IP.from_digits(3232235777)
```
### 十六进制IP
::: tip 十六进制IP
`from_hex(hex_str)`
:::
```python [from_hex.py]
from sch import IP

ip = IP.from_hex('C0A80101')
```
### 二进制IP
::: tip 二进制IP
`from_bin(bin_str)`
:::
```python [from_bin.py]
from sch import IP

ip = IP.from_bin('11000000101010000000000100000001')
```
## 计算IP
### 常规IP
::: tip 常规IP
`ip_str`
:::
```python [ip_str.py]
from sch import IP

ip = IP.from_digits(3232235777)
print(ip.ip_str)
```
::: details 输出
```
192.168.1.1
```
:::
### 数字类型IP
::: tip 数字类型IP
`ip_digits`
:::
```python [ip_digits.py]
from sch import IP

ip = IP.from_ip('192.168.1.1')
print(ip.ip_digits)
```
::: details 输出
```
3232235777
```
:::
### 十六进制IP
::: tip 十六进制IP
`ip_hex`
:::
```python [ip_hex.py]
from sch import IP

ip = IP.from_hex('C0A80101')
print(ip.ip_hex)
```
::: details 输出
```
C0A80101
```
:::
### 二进制IP
::: tip 二进制IP
`ip_bin`
:::
```python [ip_bin.py]
from sch import IP

ip = IP.from_ip('192.168.1.1')
print(ip.ip_bin)
```
::: details 输出
```
11000000101010000000000100000001
```