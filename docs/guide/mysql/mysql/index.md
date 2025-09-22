---
title: MySQL数据库
---
# MySQL数据库
::: tip 该模块依赖[mysql]
```bash
pip install sch-lib[image]
```
:::
提供了 `MySQL` 数据库的常用操作接口，简化了连接管理、表创建、数据查询、数据更新等流程，适用于需要快速对接 `MySQL` 数据库的 `Python` 项目。
## 配置文件
使用该模块前，需要在`config`目录中的配置文件中添加`mysql`配置，下面以json格式为例
::: code-group
```json [config/config.json]
{
  "mysql": {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "pass": "12345678",
    "name": "root"
  }
}
```
```toml [config/config.toml]
[mysql]
host = "localhost"
port = 3306
user = "root"
pass = "12345678"
name = "root"
```
:::
## 初始化MySQL对象
::: tip MySQL
`MySQL(config: Config, echo: bool = False)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| config | Config | 配置对象 |
| echo | bool | 是否输出MySQL执行日志 |

```python
from sch.mysql import MySQL
from sch.config import Config

config = Config.load_json()
mysql = MySQL(config.mysql)
```
## 连接数据库
::: tip connect
`connect()`
:::
连接数据库，该操作在初始化对象时自动执行，无需手动调用。
## 设置输出日志
::: tip 设置输出日志
`set_echo(echo: bool)`
:::
设置是否输出MySQL执行日志。
## 创建表
::: tip 创建表
`create_table(table: Table)`
:::
创建表，`Table`对象参考[MySQL表](../table)
::: code-group
```python [main.py]
from .table import UserList
from sch import Config, MySQL

config = Config.load_json()
mysql = MySQL(config)
mysql.create_table(UserList)
```
```python [table.py]
from sch import table

UserList = table(
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
查询数据，`Table`对象参考[MySQL表](../table)，`*where`为查询条件，可以指定多个条件。
## 查询数据是否存在
::: tip 查询数据是否存在
`exist(table: Table, *where)`
:::
查询数据是否存在，`Table`对象参考[MySQL表](../table)，`*where`为查询条件，可以指定多个条件。
## 插入数据
::: tip 插入数据
`insert(table: Table, values: dict, commit: bool = True)`
:::
插入数据，`Table`对象参考[MySQL表](../table)，`values`为插入数据，`commit`为是否立即提交，默认为`True`。
## 更新数据
::: tip 更新数据
`update(table: Table, values: dict, *where, commit: bool = True)`
:::
更新数据，`Table`对象参考[MySQL表](../table)，`values`为更新数据，`*where`为更新条件，可以指定多个条件，`commit`为是否立即提交，默认为`True`。
## 删除数据
::: tip 删除数据
`delete(table: Table, *where, commit: bool = True)`
:::
删除数据，`Table`对象参考[MySQL表](../table)，`*where`为删除条件，可以指定多个条件，`commit`为是否立即提交，默认为`True`。
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
查询表是否存在，`Table`对象参考[MySQL表](../table)。
## 删除表
::: tip 删除表
`drop_table(table: Table)`
:::
删除表，`Table`对象参考[MySQL表](../table)。