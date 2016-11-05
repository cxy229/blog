---
layout     : post
title      : sqlalchemy mysql 中文问题
categories : [sqlalchemy]
tags       : [notes]
---

### 添加`?charset=utf8` 就可以正常插入查找中文了
```
 'mysql+pymysql://uid:pwd@localhost/mydb?charset=utf8'
```
