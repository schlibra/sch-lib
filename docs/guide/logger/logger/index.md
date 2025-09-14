---
title: 日志处理类
---
# 日志处理类
可以更方便的记录程序运行日志，并对日志进行分析。这个类在初始化时，已经设置了默认日志级别、日志输出格式，默认开启文件日志和控制台日志。
## 初始化日志处理类
::: tip 日志处理类
`Logger(name: str, level: int|str)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| name | str | 日志名称，用于区分不同模块的日志 |
| level | int/str | 日志级别，可以是整数或字符串，字符串范围为`DEBUG`、`INFO`、`WARNING`、`ERROR`、`CRITICAL`，默认为`INFO` |
```python
from sch.logger import Logger
logger = Logger('Main')
```
## 输出日志
### 输出普通日志
::: tip 输出普通日志
`logger.info(message: str)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| message | str | 日志内容 |
```python
logger.info('Hello, world!')
```
::: details 输出日志效果
```
2021-08-12 10:20:30,123 [Main] INFO: Hello, world!
```
:::
### 输出调试日志
::: tip 输出调试日志
`logger.debug(message: str)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| message | str | 日志内容 |
```python
logger.debug('This is a debug message.')
```
::: details 输出日志效果
```
2021-08-12 10:20:30,123 [Main] DEBUG: This is a debug message.
```
:::
### 输出警告日志
::: tip 输出警告日志
`logger.warning(message: str)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| message | str | 日志内容 |
```python
logger.warning('This is a warning message.')
```
::: details 输出日志效果
```
2021-08-12 10:20:30,123 [Main] WARNING: This is a warning message.
```
:::
### 输出错误日志
::: tip 输出错误日志
`logger.error(message: str)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| message | str | 日志内容 |
```python
logger.error('This is an error message.')
```
::: details 输出日志效果
```
2021-08-12 10:20:30,123 [Main] ERROR: This is an error message.
```
:::
### 输出严重错误日志
::: tip 输出严重错误日志
`logger.critical(message: str)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| message | str | 日志内容 |
```python
logger.critical('This is a critical error message.')
```
::: details 输出日志效果
```
2021-08-12 10:20:30,123 [Main] CRITICAL: This is a critical error message.
```
:::