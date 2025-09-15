---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "SCH-Lib-文档"
  text: "sch lib docs"
  tagline: 轻松使用Python进行开发
  actions:
    - theme: brand
      text: 开始使用
      link: /guide/introduction
    - theme: alt
      text: 文档
      link: /

features:
  - title: 配置文件管理
    details: 通过Config类对配置文件进行管理，支持多种格式的配置文件，如JSON、YAML、INI等。
    icon: ⚙️
  - title: 日志管理
    details: 通过Log类对日志进行管理
    icon: 📄
  - title: 数据库管理
    details: 对SQLAlchemy进行封装，简化数据库操作，目前支持MySQL
    icon: 📦
  - title: 对象存储管理
    details: 通过s3对对象存储进行管理，支持文件上传，下载，删除等操作
    icon: 💾
  - title: 头像生成
    details: 生成Github风格头像，根据输入文本计算hash值，生成不同颜色的头像
    icon: 🖼️
---
## 使用sch-lib轻松进行开发
```bash [安装依赖]
pip install sch-lib[mysql]
```
::: code-group
```python [main.py]
from sch.config import Config
from sch.mysql import MySQL

config = Config.load_json() # 加载配置 [!code focus]
mysql = MySQL(config) # 连接数据库 [!code focus]
```
```json [config/config.json]
{
  "mysql": {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "pass": "123456",
    "name": "root"
  }
}
```
:::