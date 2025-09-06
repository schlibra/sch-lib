---
title: 配置文件加载类
---

# 配置文件加载类
配置文件加载类用于加载配置文件，支持多种格式的配置文件，如：JSON、YAML、INI、TOML。获取键值支持使用`.`符号进行层级访问。
## 加载配置
### 加载JSON格式配置文件
::: tip 加载JSON格式配置文件
`load_json(config_file: str='config/config.json')`
:::
如果需要自定义配置文件路径，可以传入`config_file`参数。
```python
from sch.config import Config

config = config.load_json()
```
### 加载YAML格式配置文件
::: tip 加载YAML格式配置文件
`load_yaml(config_file: str='config/config.yaml')`
:::
如果需要自定义配置文件路径，可以传入`config_file`参数。
```python
from sch.config import Config

config = config.load_yaml()
```
### 加载INI格式配置文件
::: tip 加载INI格式配置文件
`load_ini(config_file: str='config/config.ini')`
:::
如果需要自定义配置文件路径，可以传入`config_file`参数。
```python
from sch.config import Config

config = config.load_ini()
```
### 加载TOML格式配置文件
::: tip 加载TOML格式配置文件
`load_toml(config_file: str='config/config.toml')`
:::
如果需要自定义配置文件路径，可以传入`config_file`参数。
```python
from sch.config import Config

config = config.load_toml()
```
## 获取键值
::: tip 获取键值
`get(key: str)`
:::
获取键值，支持使用`.`符号进行层级访问。
```python
from sch.config import Config

config = config.load_json()
config.get('mysql.host')
```
::: details 输出内容
`localhost`
:::