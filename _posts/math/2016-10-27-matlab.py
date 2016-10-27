---
layout     : post
title      : matlab
categories : [math]
tags       : [notes]
---

### 资料
- [官方自带教程](https://cn.mathworks.com/help/matlab/getting-started-with-matlab.html)

### tips

#### 格式化输出
- `disp(sprintf('%0.6f',a))`

#### Moving data around

##### 加载数据
- `a = load('file_name')`

##### 保存变量
- `save test.mat variable_name;`
- `save test.txt variable_name -ascii;`

#### 伪操作

##### 清除
- `clear variablename`

##### show variables
- `whos`


