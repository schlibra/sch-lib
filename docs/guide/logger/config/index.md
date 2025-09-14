---
title: 日志配置
---

# 日志配置
通过日志配置类对日志进行配置，包括日志级别、日志文件路径等。
## 设置属性
日志配置类提供了以下属性：
### 启用日志
::: info 设置启用日志
`set_enable(_enable: bool)`
> _enable: 是否启用日志，True为启用，False为禁用。禁用后所有日志将不会输出以及写入日志文件。
:::

```python
from sch import LoggerConfig

LoggerConfig.set_enable(True)
```

## 获取属性