---
title: 日志配置
---

# 日志配置
通过日志配置类对日志进行配置，包括日志级别、日志文件路径等。
## 设置属性
日志配置类提供了以下属性：
### 设置启用日志
::: tip 设置启用日志
`set_enable(_enable: bool)`
> _enable: 是否启用日志，True为启用，False为禁用。禁用后所有日志将不会输出以及写入日志文件。
:::

```python
from sch import LoggerConfig

LoggerConfig.set_enable(True)
```
### 设置日志级别
::: tip 设置日志级别
`set_level(_level: str)`
> _level: 日志级别，可选值为`DEBUG`、`INFO`、`WARNING`、`ERROR`、`CRITICAL`。
:::
```python
from sch import LoggerConfig

LoggerConfig.set_level('DEBUG')
```
### 设置日志格式
::: tip 设置日志格式
`set_format(_format: str)`
> _format: 日志格式，默认值为`%(asctime)s - %(name)s - %(levelname)s - %(message)s`。
:::
```python
from sch import LoggerConfig

LoggerConfig.set_format('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```
### 设置启用终端输出
::: tip 设置启用终端输出
`set_enable_console(_enable: bool)`
> _enable: 是否启用终端输出，True为启用，False为禁用。
:::
```python
from sch import LoggerConfig

LoggerConfig.set_enable_console(True)
```
### 设置启用文件输出
::: tip 设置启用文件输出
`set_enable_file(_enable: bool)`
> _enable: 是否启用文件输出，True为启用，False为禁用。
:::
```python
from sch import LoggerConfig

LoggerConfig.set_enable_file(True)
```
### 设置日志文件路径
::: tip 设置日志文件路径
`set_file_path(_file_path: str)`
> _file_path: 日志文件路径。
:::
```python
from sch import LoggerConfig

LoggerConfig.set_file_path('log/main.log')
```
## 获取属性
### 获取启用日志
::: tip 获取启用日志
`get_enable() -> bool`
:::
```python
from sch import LoggerConfig

if LoggerConfig.get_enable():
    print('启用日志')
else:
    print('禁用日志')
```
### 获取日志级别
::: tip 获取日志级别
`get_level() -> str`
:::
```python
from sch import LoggerConfig

print(LoggerConfig.get_level())
```
### 获取日志格式
::: tip 获取日志格式
`get_format() -> str`
:::
```python
from sch import LoggerConfig

print(LoggerConfig.get_format())
```
### 获取启用终端输出
::: tip 获取启用终端输出
`get_enable_console() -> bool`
:::
```python
from sch import LoggerConfig

if LoggerConfig.get_enable_console():
    print('启用终端输出')
else:
    print('禁用终端输出')
```
### 获取启用文件输出
::: tip 获取启用文件输出
`get_enable_file() -> bool`
:::
```python
from sch import LoggerConfig

if LoggerConfig.get_enable_file():
    print('启用文件输出')
else:
    print('禁用文件输出')
```
### 获取日志文件路径
::: tip 获取日志文件路径
`get_file_path() -> str`
:::
```python
from sch import LoggerConfig

print(LoggerConfig.get_file_path())
```