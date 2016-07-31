---
layout     : post
title      : linux-command-line
categories : [linux]
tags       : [notes]
---
### linux文件与目录管理
* ls
>* ls -al|less

* cp
>* cp -p test.rb /home/test   #将test.rb copy到test目录，并且保留原文件的属
>* cp -r Dir/ /home/test      #将Dir目录copy到test目录下

* mv
>* mv abc abc.php  #将abc移动成abc.php

* rename
>*

#### 取得路径的文件名与目录名
* basename
* dirname

#### 查看文件内容
* cat
>* cat -n test     #显示行号
>* cat -A test    #换行$  [tab]^I

* tac
* nl
*  less
>* less -N test  #显示行号

* head
* tail
* od

#### 修改文件时间和创建新文件
* touch

#### 新创建文件和目录的默认权限
* umask

#### 文件的特殊权限
* chattr #修改
* lsattr #显示

#### 文件特殊权限:SUID SGID SBIT

#### 查看文件类型
* file

#### 命令与文件名的查询
* which #寻找“执行文件”的位置
查找文件（updatedb 更新数据库）
 * whereis
 * locate
 * find
