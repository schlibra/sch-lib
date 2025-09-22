---
title: 安装
---
# 安装 {#installation}
## 环境要求 {#environment-requirements}
- Python 3.9+
- pip
## 安装方式 {#installation-method}
### 通过 pip 安装 {#install-via-pip}
推荐使用该方法安装，步骤较为简单。下面命令默认安装最少依赖，根据需要可以安装其他依赖。若不安装其他依赖，仍可以使用`sch.config`、`sch.logger`模块
```shell
pip install sch-lib
```
### 通过源码安装 {#install-via-source}
```shell {3}
git clone https://github.com/sch-lib/sch-lib.git
cd sch-lib
python setup.py install
```
### 通过whl包安装 {#install-via-wheel}
从[release页面](https://github.com/schlibra/sch-lib/releases)下载whl包，然后通过pip安装
```shell
pip install sch-lib-x.x.x-py3-none-any.whl
```
## 安装其他依赖 {#install-other-dependencies}
### 全部依赖 {#all-dependencies}
::: tip 提示
执行这个可以安装下面的所有依赖，即可以使用全部模块
:::
```bash
pip install sch-lib[all]
```
### mysql依赖 {#mysql-dependency}
安装[mysql]依赖后才可以使用`sch.mysql`模块
```bash
pip install sch-lib[mysql]
```
### request依赖 {#request-dependency}
安装[request]依赖后才可以使用`sch.image_api`、`sch.openlist`、`sch.util.mermaid`模块
```bash
pip install sch-lib[request]
```
### s3依赖 {#s3-dependency}
安装[s3]依赖后才可以使用`sch.s3`模块
```bash
pip install sch-lib[s3]
```
### image依赖 {#image-dependency}
安装[image]依赖后才可以使用`sch.avatar`模块
```bash
pip install sch-lib[image]
```
### qrcode依赖 {#qrcode-dependency}
安装[qrcode]依赖后才可以使用`sch.util.qrcode`模块
```bash
pip install sch-lib[qrcode]
```
### clip依赖 {#clip-dependency}
安装[clip]依赖后才可以使用`sch.util.clip`模块
```bash
pip install sch-lib[clip]
```
### markdown依赖 {#markdown-dependency}
安装[markdown]依赖后才可以使用`sch.util.markdown`模块
```bash
pip install sch-lib[markdown]
```