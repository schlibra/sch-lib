---
title: 创建表对象
---
# 创建表对象
::: tip 创建表对象
`table(name, columns)`
:::
创建表对象需要指定表名和列信息。
| 属性 | 类型 | 描述 |
| --- | --- | --- |
| name | string | 表名 |
| columns | array | 列信息 |

## 列信息
列信息是一个数组，数组的每个元素都是一个元组，包含以下属性：
> (列名, 列类型, 列选项)
列类型可以为以下类型（类型可传入字符串或python的标准类型对象）：
- `string`：字符串类型 可传入`str`/`'str'`/`'string'`
- `integer`：整型类型 可传入`int`/`'int'`/`'integer'`
- `float`：浮点型类型 可传入`float`/`'float'`
- `boolean`：布尔类型 可传入`bool`/`'bool'`/`'boolean'`
- `date`：日期类型 可传入`datetime.date`/`'date'`
- `datetime`：日期时间类型 可传入`datetime.datetime`/`'datetime'`

列选项可以是布尔值(bool)或整数(int)，具体含义如下：
- bool: True时设置该列为主键，并且该值可自增，False时不设置主键
- int: 设置该列的长度，仅对字符串类型有效，默认为255

## 示例
```python [table.py]
from sch import MySQL

UserList = MySQL.table(
    'user_list',
    [
        ('id', int, True),
        ('username', 'str'),
        ('password', 'string', 200),
        ('create_time', 'datetime')
    ]
)
```