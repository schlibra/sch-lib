---
title: MySQL数据库
---
# MySQL数据库
提供了 `MySQL` 数据库的常用操作接口，简化了连接管理、表创建、数据查询、数据更新等流程，适用于需要快速对接 `MySQL` 数据库的 `Python` 项目。

## 1依赖环境
| 依赖库 | 说明 | 安装指令 |
| --- | --- | --- |
| `sqlalchemy` | 数据库 ORM 框架，提供核心连接与执行能力 | `pip install sqlalchemy` |
| `pymysql` | MySQL 数据库的 Python 驱动 | `pip install pymysql` |


## 2初始化数据库
```python
# 导入依赖
from sch.mysql import MySQL  # 导入封装的MySQL类

# 1. 配置数据库连接信息（替换为项目实际配置）
db_config = {
    "mysql.user": "<username>",          # 数据库用户名
    "mysql.pass": "<password>", # 数据库密码（如本地测试可填实际密码）
    "mysql.host": "localhost",     # 数据库主机（本地默认127.0.0.1）
    "mysql.port": 3306,            # 数据库端口（默认3306）
    "mysql.name": "<databasename>"        # 数据库名称（需提前在MySQL中创建）
}

# 2. 初始化MySQL实例（echo=True开启SQL打印，调试时用）
try:
    mysql = MySQL(config=db_config, echo=True)
    print("MySQL实例初始化成功")
except Exception as e:
    print(f"MySQL实例初始化失败：{str(e)}")
    raise  # 抛出异常中断程序（根据需求调整）

# 3. 查询并打印MySQL版本(可选)
try:
    version = mysql.get_version()
    print(f"当前MySQL数据库版本：{version}")  # 示例输出：当前MySQL数据库版本：8.0.32
except Exception as e:
    print(f"版本查询失败：{str(e)}")
```

## 3创建数据表
```python
# 完整导入依赖
from sqlalchemy import MetaData, Column, Integer, String, Table  # SQLAlchemy表结构相关
from sch.mysql import MySQL  # 导入封装的MySQL类

# 1. 初始化MySQL实例（复用上方的初始化）
db_config = {
    "mysql.user": "<username>",          # 数据库用户名
    "mysql.pass": "<password>", # 数据库密码（如本地测试可填实际密码）
    "mysql.host": "localhost",     # 数据库主机（本地默认127.0.0.1）
    "mysql.port": 3306,            # 数据库端口（默认3306）
    "mysql.name": "<databasename>"        # 数据库名称（需提前在MySQL中创建）
}

mysql = MySQL(config=db_config, echo=True)

# 2. 定义表结构（以用户表users为例）
# MetaData用于管理表集合，Table定义具体表结构
metadata = MetaData()
user_table = Table(
    "users",  # 表名
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),  # 主键（自增）
    Column("name", String(50), nullable=False),  # 用户名（非空，最大长度50）
    Column("age", Integer, nullable=True),       # 年龄（可空）
    Column("email", String(100), nullable=True, unique=True)  # 邮箱（可空，唯一）
)

# 3. 调用create_table方法以创建表
try:
    mysql.create_table(table=user_table)
    print(f"表 {user_table.name} 创建成功")
except Exception as e:
    print(f"表创建失败：{str(e)}")
    mysql.connection.rollback()  # 失败时回滚事务
```
## 4查询数据库中数据
```python
# 完整导入依赖
from sqlalchemy import MetaData, Column, Integer, String, Table, select  # 含查询语句依赖
from sch.mysql import MySQL  # 导入封装的MySQL类

# 1. 初始化MySQL实例 + 定义表结构（查询需关联表结构，或直接用SQL字符串）
db_config = {
    "mysql.user": "<username>",        
    "mysql.pass": "<password>", 
    "mysql.host": "localhost",     
    "mysql.port": 3306,           
    "mysql.name": "<databasename>"        
}
mysql = MySQL(config=db_config, echo=True)

# 定义与数据库中一致的表结构（用于SQLAlchemy表达式查询）
metadata = MetaData()
user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("age", Integer),
    Column("email", String(100))
)
```
### 场景1：单条查询（用SQL字符串）

```python
try:
    # 查询id=1的用户（SQL字符串）
    single_sql = "SELECT id, name, age, email FROM users WHERE id = 1"
    single_result = mysql.fetchone(single_sql)
    
    if single_result:
        # 两种取值方式：索引取值 + 属性名取值
        print(f"单条查询结果：")
        print(f"  索引取值：ID={single_result[0]}, 姓名={single_result[1]}, 年龄={single_result[2]}")
        print(f"  属性取值：ID={single_result.id}, 姓名={single_result.name}, 邮箱={single_result.email}")
    else:
        print("单条查询：未找到id=1的用户")
except Exception as e:
    print(f"单条查询失败：{str(e)}")
```
### 场景2：批量查询（用SQLAlchemy表达式）
```python
try:
    # 构建查询：年龄>18且邮箱不为空的用户（按id降序）
    batch_query = select(
        user_table.c.id, 
        user_table.c.name, 
        user_table.c.age
    ).where(
        (user_table.c.age > 18) & (user_table.c.email.isnot(None))
    ).order_by(
        user_table.c.id.desc()
    )
    
    # 执行批量查询
    batch_results = mysql.fetchall(batch_query)
    print(f"\n批量查询结果（共{len(batch_results)}条）：")
    for idx, result in enumerate(batch_results, 1):
        print(f"  第{idx}条：ID={result.id}, 姓名={result.name}, 年龄={result.age}")
except Exception as e:
    print(f"批量查询失败：{str(e)}")
```
## 5数据的更新（包含：插入 + 更新 + 删除）
```python
# 完整导入依赖
from sch.mysql import MySQL  # 导入封装的MySQL类

# 1. 初始化MySQL实例
db_config = {
    "mysql.user": "<username>",        
    "mysql.pass": "<password>", 
    "mysql.host": "localhost",     
    "mysql.port": 3306,           
    "mysql.name": "<databasename>"        
}
mysql = MySQL(config=db_config, echo=True)
```
### 场景1：插入数据（自动提交）
```python
try:
    # 插入1条用户数据（自动提交事务）
    insert_sql = """
        INSERT INTO users (name, age, email) 
        VALUES ('Alice', 25, 'alice@example.com')
    """
    mysql.update(statement=insert_sql, commit=True)  # commit=True自动提交
    print("数据插入成功")
except Exception as e:
    print(f"数据插入失败：{str(e)}")
    if not mysql.connection.in_transaction():
        mysql.connection.rollback()
```
### 场景2：更新数据（手动提交）
```python
try:
    # 批量更新：将姓名为Alice的用户年龄改为26（暂不提交）
    update_sql = """
        UPDATE users 
        SET age = 26 
        WHERE name = 'Alice'
    """
    mysql.update(statement=update_sql, commit=False)  # commit=False暂不提交
    
    # 补充其他操作（示例：更新邮箱）
    update_email_sql = """
        UPDATE users 
        SET email = 'alice_new@example.com' 
        WHERE name = 'Alice'
    """
    mysql.update(statement=update_email_sql, commit=False)
    
    # 所有操作完成后，手动提交事务
    mysql.commit()
    print("数据更新成功")
except Exception as e:
    print(f"数据更新失败：{str(e)}")
    mysql.connection.rollback()  # 失败时回滚所有未提交操作
```
### 场景3：删除数据（用execute方法）
```python
try:
    # 删除姓名为Alice的用户（execute内部调用update，默认commit=True）
    delete_sql = "DELETE FROM users WHERE name = 'Alice'"
    mysql.execute(statement=delete_sql)  # 无需手动commit
    print("数据删除成功")
except Exception as e:
    print(f"数据删除失败：{str(e)}")
    mysql.connection.rollback()

# 最终关闭连接（避免资源泄漏）
finally:
    mysql.connection.close()
    mysql.engine.dispose()
    print("数据库连接已关闭")
```
##  **_6注意！！！_**
#### 1.关闭连接
本工具不包含自动关闭连接，需要手动关闭以防止数据泄露，代码如下：
```python
mysql.connection.close()  # 关闭当前连接
mysql.engine.dispose()    # 释放引擎连接池资源
```
#### 2.事务控制：
`update` 和 `execute` 方法默认 `commit=True`，即执行后自动提交事务。
若需**批量操作**（如多步写操作），建议将 `commit` 设为 `False`，所有操作完成后手动调用 `mysql.commit()`，避免部分操作失败导致数据不一致。

#### 3.配置参数校验：
初始化时需确保 `config` 字典包含所有必需键。






