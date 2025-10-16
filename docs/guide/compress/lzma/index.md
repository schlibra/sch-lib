---
title: Lzma 压缩
---
# Lzma 压缩
通过Lzma对文本或文件进行压缩
## 压缩文本
:::tip 压缩文本
compress_text(text: str, level: int = 9) -> str
:::
```python
from sch import Lzma

data = Lzma.compress_text("hello world")
print(data)
```
:::details 输出内容
`/Td6WFoAAATm1rRGAgAhARYAAAB0L+WjAQAKaGVsbG8gd29ybGQAANpSI+/NfgNTAAEjC8Ib/QkftvN9AQAAAAAEWVo=`
::: 
## 解压文本
:::tip 解压文本
decompress_text(data: str) -> str
:::
```python
from sch import Lzma

data = "/Td6WFoAAATm1rRGAgAhARYAAAB0L+WjAQAKaGVsbG8gd29ybGQAANpSI+/NfgNTAAEjC8Ib/QkftvN9AQAAAAAEWVo="
text = Lzma.decompress_text(data)
print(text)
```
:::details 输出内容
`hello world`
:::
## 压缩文件
:::tip 压缩文件
compress_file(input_file: str, output_file: str, level: int = 9)
:::
```python
from sch import Lzma

Lzma.compress_file("input.txt", "output.gz")
```
:::tip 解压文件
decompress_file(input_file: str, output_file: str)
:::
```python
from sch import Lzma

Lzma.decompress_file("input.gz", "output.txt")
```

