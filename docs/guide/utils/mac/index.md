---
title: MAC地址信息
---
# MAC地址信息
通过MAC地址获取厂家信息
## MAC厂家信息查询
::: tip MAC厂家信息查询
`get_mac_info(mac_address)`
:::
传入`mac_address`参数，可以使用`:`/`.`/`-`连接的MAC地址，返回MAC地址对应的厂家信息。
```python [mac_info.py]
from sch import get_mac_info

print(get_mac_info('D4:5D:64:11:22:33'))
```
::: details 输出
```
ASUSTek COMPUTER INC.
15,Li-Te Rd., Peitou, Taipei 112, Taiwan
Taipei Taiwan 112
Taiwan
```
:::