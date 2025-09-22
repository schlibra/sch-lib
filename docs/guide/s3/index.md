---
title: S3对象存储
---
# S3对象存储
S3（Simple Storage Service，简单存储服务）是AWS提供的一种对象存储服务，提供高可靠性、高可用性、安全性、可扩展性和低成本的云存储服务。S3提供了一个RESTful API接口，可以用来存储和检索任意数量和大小的对象。
::: tip 该模块依赖[s3]
```bash
pip install sch-lib[s3]
```
:::
## 配置文件
在使用S3对象存储之前，需要先在配置文件中配置相关信息。
::: code-group

```json [config/config.json]
{
  "s3": {
    "endpoint": "http[s]://s3.example.com",
    "access_key": "your_access_key",
    "secret_key": "your_secret_key"
  }
}
```
```toml [config/config.toml]
[s3]
endpoint = "http[s]://s3.example.com"
access_key = "your_access_key"
secret_key = "your_secret_key"
```
```yaml [config/config.yaml]
s3:
  endpoint: "http[s]://s3.example.com"
  access_key: "your_access_key"
  secret_key: "your_secret_key"
```
:::
## 初始化对象
::: tip S3
`S3(config: Config)`
:::
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| config | Config | 配置对象 |
```python [s3.py]
from sch import Config, S3

config = Config.load_json()
s3 = S3(config)
```
## 获取存储桶
::: tip 获取存储桶
`list_buckets()`
:::
## 设置存储桶
::: tip 设置存储桶
`set_bucket(bucket_name: str)`
:::
设置存储桶后，就可以在该存储桶下上传、下载、删除对象了。
## 读取对象
::: tip 读取对象
`read_file(key: str)`
:::
## 上传对象
::: tip 上传对象
`write_file(key: str, data: str|bytes)`
:::
## 删除对象
::: tip 删除对象
`delete_file(key: str)`
:::