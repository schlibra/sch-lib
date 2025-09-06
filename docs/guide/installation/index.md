---
title: 安装
---
# 安装 {#installation}
## 环境要求 {#environment-requirements}
- Python 3.9+
- pip
# 安装方式 {#installation-method}
## 通过 pip 安装 {#install-via-pip}
推荐使用该方法安装，步骤较为简单
```shell
pip install sch-lib
```
## 通过源码安装 {#install-via-source}
```shell {3}
git clone https://github.com/sch-lib/sch-lib.git
cd sch-lib
python setup.py install
```
## 通过whl包安装 {#install-via-wheel}
从[release页面](https://github.com/schlibra/sch-lib/releases)下载whl包，然后通过pip安装
```shell
pip install sch-lib-x.x.x-py3-none-any.whl
```