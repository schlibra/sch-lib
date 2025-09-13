# SCH-Lib

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.1-orange.svg)](https://github.com/schlibra/sch-lib)

SCH-Lib 是一个基于 Python 的实用工具库，封装了日常开发中常用的功能模块，旨在提高开发效率和代码质量。

## ✨ 特性

- 🔧 **配置文件管理** - 支持 JSON、YAML、INI 等多种格式的配置文件管理
- 📝 **日志管理** - 提供灵活的日志记录和配置功能
- 🗄️ **数据库管理** - 基于 SQLAlchemy 的 MySQL 数据库操作封装
- ☁️ **对象存储** - S3 兼容的对象存储服务管理
- 🖼️ **头像生成** - GitHub 风格的头像生成器
- 🔐 **实用工具** - Base64 编解码、密码隐藏等常用工具

## 📦 安装

### 环境要求

- Python 3.9+
- pip

### 通过 pip 安装（推荐）

```bash
pip install sch-lib
```

### 通过源码安装

```bash
git clone https://github.com/schlibra/sch-lib.git
cd sch-lib
pip install .
```

### 通过 wheel 包安装

从 [Releases 页面](https://github.com/schlibra/sch-lib/releases) 下载对应的 wheel 包：

```bash
pip install sch-lib-x.x.x-py3-none-any.whl
```

## 🚀 快速开始

```python
from sch import Config, MySQL, Logger, generate_avatar

# 配置文件管理
config = Config.load_json('config.json')

# 数据库连接
mysql = MySQL(config)
version = mysql.get_version()

# 日志记录
logger = Logger('app')
logger.info('应用启动成功')

# 头像生成
generate_avatar('username')
```

## 📖 功能模块

### 配置文件管理 (Config)

支持多种格式的配置文件加载和管理：

```python
from sch import Config, ConfigConverter

# 加载 JSON 配置
config = Config.load_json('config.json')

# 配置格式转换
converter = ConfigConverter.load_json()
converter.save_yaml()
```

### 数据库管理 (MySQL)

基于 SQLAlchemy 的 MySQL 数据库操作：

```python
from sch import MySQL, Config

# 加载配置文件
config = Config.load_json()

# 初始化数据库连接
mysql = MySQL(config)

# 获取数据库版本
version = mysql.get_version()

# 执行查询
result = mysql.execute("SELECT * FROM users")
```

### 日志管理 (Logger)

灵活的日志记录功能：

```python
from sch import Logger

# 初始化日志器
logger = Logger('app')

# 记录日志
logger.info('这是一条信息日志')
logger.error('这是一条错误日志')
```

### 对象存储 (S3)

S3 兼容的对象存储服务：

```python
from sch import S3, Config

# 加载配置文件
config = Config.load_json()

# 初始化 S3 客户端
s3 = S3(config)

# 设置存储桶
s3.set_bucket("bucket")

# 上传文件
s3.write_file("/test.txt", "Hello, world!")

# 下载文件
s3.read_file("/test.txt")

# 删除文件
s3.delete_file("/test.txt")
```

### 头像生成

生成 GitHub 风格的头像：

```python
from sch import generate_avatar

# 生成头像
generate_avatar()
```

### 实用工具

常用的编码和安全工具：

```python
from sch import base64_encode, base64_decode, password_hide

# Base64 编解码
encoded = base64_encode('hello world')
decoded = base64_decode(encoded)

# 密码隐藏
hidden = password_hide('my_secret_password')
```

## 🔧 命令行工具

### 定时任务

```bash
run-interval
```

### LED 控制

```bash
led
```

## 📚 文档

详细的文档和 API 参考请访问：[文档网站](https://sch-lib.schhz.cn/)

## 🤝 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 📋 依赖

主要依赖包：

- `boto3>=1.40.10` - AWS SDK
- `bs4>=0.0.2` - HTML 解析
- `cryptography>=45.0.6` - 加密工具
- `pillow>=11.3.0` - 图像处理
- `pymysql>=1.1.1` - MySQL 连接器
- `pyyaml>=6.0.2` - YAML 解析器
- `requests>=2.32.4` - HTTP 请求
- `sqlalchemy>=2.0.43` - ORM 框架

## 📝 许可证

本项目采用 GPL-2.0 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

## 👤 作者

**schlibra**

- Email: [schlibra@163.com](mailto:schlibra@163.com)
- GitHub: [@schlibra](https://github.com/schlibra)

## 🙏 致谢

感谢所有为此项目做出贡献的开发者！

---

如果您觉得这个项目有用，请给它一个 ⭐️！
