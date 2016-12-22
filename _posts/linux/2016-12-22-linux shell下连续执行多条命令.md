---
layout     : post
title      : linux shell下连续执行多条命令
categories : [linux]
tags       : [notes]
---

## 使用`&&`

```
sudo apt-get update && sudo apt-get install python3-pandas python3-pip
```

- 如果命令执行时出错了，后面的命令便不会执行。
<br><img src="{{ site.blog.qiniu }}2810b6110849d441c7e5af6830eb2c70.png" height="400"><br>

## 使用`;`

```
sudo apt-get update ; sudo apt-get install python3-pandas python3-pip
```

- 全部执行，即使前面的命令错了，后面的命令也会执行。
<br><img src="{{ site.blog.qiniu }}528ae4799a5fca8ae70f75bd0db328b9.png" height="400"><br>
