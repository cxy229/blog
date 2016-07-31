---
layout     : post
title      : git clone problem
categories : git
tags       : [notes]
---
### 错误信息:
>Failed to execute "git ls-remote --tags --heads git://github.com/twbs/bootstrap-sass.git", exit code of #128 fatal: unable to connect to github.com: github.com[0: 192.30.252.130]: errno=Connection timed out

### 解决方法:
```
git config --global url."https://".insteadOf git://
```
