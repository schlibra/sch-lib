---
title: 快速开始
---
# 快速开始
## 加载配置文件
> 首先需要创建一个配置文件，一般存放在项目根目录下的`config`目录中，文件名为`config.[ext]`，拓展名可以是`yaml`、`json`、`toml`、`ini`。
创建完配置文件后，就可以通过下面的代码来加载配置文件。下面以`json`格式的配置文件为例。
```python {4}
from sch.config import Config

config = Config()
config.load_json()
```
此时配置文件就加载完成了，要获取全部配置可以调用`config.config`属性。
```python
print(config.config)
```
::: details 输出结果
```json
{
  "mysql": {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "password",
    "database": "test"
  }
}
```
:::
如果要获取某个配置的值，可以调用`config.get`方法，键名可以是用`.`分隔的多级键名。例如下面获取`mysql.host`的值：
```python
print(config.get('mysql.host'))
```
::: details 输出结果
`localhost`
:::
## 连接数据库
可以直接通过刚才的`config`对象来连接数据库，示例如下：
```python {3}
from sch.mysql import MySQL

mysql = MySQL(config)
```