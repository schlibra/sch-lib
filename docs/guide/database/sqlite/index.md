---
title: SQLite数据库
---
# SQLite数据库
::: tip 该模块依赖[db]
```bash
pip install sch-lib[db]
```
:::
提供了 `SQLite` 数据库的常用操作接口，简化了连接管理、表创建、数据查询、数据更新等流程，适用于需要快速对接 `SQLite` 数据库的 `Python` 项目。
## 初始化SQLite对象
::: tip SQLite
`SQLite(filename, echo: bool = False)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| filename | str | SQLite数据库文件路径 |
| echo | bool | 是否输出SQLite执行日志 |

```python
from sch import SQLite

sqlite = SQLite("test.db")
```
## 连接数据库
::: tip connect
`connect()`
:::
连接数据库，该操作在初始化对象时自动执行，无需手动调用。
## 输出日志
::: tip 输出日志
`echo`
:::
设置/获取是否输出SQLite执行日志。
```python
from sch import SQLite

sqlite = SQLite()
sqlite.echo = True
print(sqlite.echo)  # True
```
## 创建表
::: tip 创建表
`create_table(table: Table)`
:::
创建表，`Table`对象参考[SQLite表](table)
::: code-group
```python [main.py]
from .table import UserList
from sch import SQLite

sqlite = SQLite()
sqlite.create_table(UserList)
```
```python [table.py]
from sch import SQLite

UserList = SQLite.table(
    "user_list",
    [
        ('id', int, True),
        ('username', str, 100),
        ('password', str, 100),
    ]
)
```
:::
## 通过语句获取所有数据
::: tip 通过语句获取所有数据
`fetchall(statement: Executable|str)`
:::
通过语句获取所有数据，statement可以是`Executable`对象或str类型的SQL语句。
## 通过语句获取单条数据
::: tip 通过语句获取单条数据
`fetchone(statement: Executable|str)`
:::
通过语句获取单条数据，statement可以是`Executable`对象或str类型的SQL语句。
## 查询数据
::: tip 查询数据
`select(table: Table, *where)`
:::
查询数据，`Table`对象参考[SQLite表](table)，`*where`为查询条件，可以指定多个条件。
## 查询数据是否存在
::: tip 查询数据是否存在
`exist(table: Table, *where)`
:::
查询数据是否存在，`Table`对象参考[SQLite表](table)，`*where`为查询条件，可以指定多个条件。
## 插入数据
::: tip 插入数据
`insert(table: Table, values: dict, commit: bool = True)`
:::
插入数据，`Table`对象参考[SQLite表](table)，`values`为插入数据，`commit`为是否立即提交，默认为`True`。
## 更新数据
::: tip 更新数据
`update(table: Table, values: dict, *where, commit: bool = True)`
:::
更新数据，`Table`对象参考[SQLite表](table)，`values`为更新数据，`*where`为更新条件，可以指定多个条件，`commit`为是否立即提交，默认为`True`。
## 删除数据
::: tip 删除数据
`delete(table: Table, *where, commit: bool = True)`
:::
删除数据，`Table`对象参考[SQLite表](table)，`*where`为删除条件，可以指定多个条件，`commit`为是否立即提交，默认为`True`。
## 执行语句
::: tip 执行语句
`execute(statement: Executable|str, commit: bool = True)`
:::
执行语句，`Executable`对象或str类型的SQL语句，`commit`为是否立即提交，默认为`True`。
## 提交执行
::: tip 提交执行
`commit()`
:::
提交执行，在执行语句时，如果`commit`为`False`，则需要手动提交。
## 获取数据库版本
::: tip 获取数据库版本
`get_version()`
:::
获取数据库版本。
## 查询表是否存在
::: tip 查询表是否存在
`table_exists(table: Table)`
:::
查询表是否存在，`Table`对象参考[SQLite表](table)。
## 删除表
::: tip 删除表
`drop_table(table: Table)`
:::
删除表，`Table`对象参考[SQLite表](table)。