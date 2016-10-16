---
layout     : post
title      : python基础1之用做calculator
categories : [python]
tags       : [notes]
---

### 初学python时做的笔记

```python
#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
```

### 用作calculator

#### 运算符
>//
>**

_  ＃最后一次表达式的值
#### 字符串
* `r  #raw strings`

```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

* """..."""or'''...'''

```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```
'+' '*'  #字符串的连接与重复
* index
* slice

```python
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```

* len()

```python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```

#### 列表
* list
 * index
 * slice
 * '+' '*'
 * append()

```python
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```
 * len()
* 列表解析

```python
#去除列表中的重复元素
l = [1,2,3,4,1,5]
l2 = []
[l2.append(i) for i in l if i not in l2]
```

#### print()
 * print()

```python
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
```
   * end

```python
>>> a, b = 0, 1
>>> while b < 1000:
...     print(b, end=',')
...     a, b = b, a+b
...
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```
