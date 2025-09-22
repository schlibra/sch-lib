---
title: 配置文件转换
---
# 配置文件转换
配置文件转换类可以将不同格式的配置文件进行转换，支持JSON、YAML、TOML、INI格式之间相互转换。
> 转换配置文件需要先加载配置文件，然后导出为目标格式。
## 加载配置文件
### 加载dict对象
::: tip 加载dict对象
`load_data(config_dict: dict)`
:::
```python {4-12}
from sch.config.convert import ConfigConverter

converter = ConfigConverter.load_data({
  "mysql": {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "password",
    "database": "test"
  }
})
```
### 加载JSON配置文件
::: tip 加载JSON配置文件
`load_json(config_file: str='config/config.json')`
:::
```python {4}
from sch.config.convert import ConfigConverter

converter = ConfigConverter.load_json()
```
### 加载YAML配置文件
::: tip 加载YAML配置文件
`load_yaml(config_file: str='config/config.yaml')`
:::
```python {4}
from sch.config.convert import ConfigConverter

converter = ConfigConverter.load_yaml()
```
### 加载TOML配置文件
::: tip 加载TOML配置文件
`load_toml(config_file: str='config/config.toml')`
:::
```python {4}
from sch.config.convert import ConfigConverter

converter = ConfigConverter.load_toml()
```
### 加载INI配置文件
::: tip 加载INI配置文件
`load_ini(config_file: str='config/config.ini')`
:::
```python {4}
from sch.config.convert import ConfigConverter

converter = ConfigConverter.load_ini()
```
### 加载XML配置文件
::: tip 加载XML配置文件
`load_xml(config_file: str='config/config.xml')`
:::
```python {4}
from sch.config.convert import ConfigConverter

converter = ConfigConverter.load_xml()
```
## 导出配置文件
### 输出dict对象
::: tip 输出dict对象
`dump_data()`
:::
```python
from sch import ConfigConverter

converter = ConfigConverter.load_json()
converter.dump_data()
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
### 导出JSON配置文件
::: tip 导出JSON配置文件
`save_json(config_file: str='config/config.json')`
:::
```python {4}
converter.save_json()
```
### 导出YAML配置文件
::: tip 导出YAML配置文件
`save_yaml(config_file: str='config/config.yaml')`
:::
```python {4}
converter.save_yaml()
```
### 导出TOML配置文件
::: tip 导出TOML配置文件
`save_toml(config_file: str='config/config.toml')`
:::
```python {4}
converter.save_toml()
```
### 导出INI配置文件
::: tip 导出INI配置文件
`save_ini(config_file: str='config/config.ini')`
:::
```python {4}
converter.save_ini()
```
### 导出XML配置文件
::: tip 导出XML配置文件
`save_xml(config_file: str='config/config.xml')`
:::
```python {4}
converter.save_xml()
```