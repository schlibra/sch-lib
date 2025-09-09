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
- `config/config.json`
```json 
{
  "mysql": {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "12345678",
    "database": "root"
  }
}
```
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
