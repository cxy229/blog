---
layout     : post
title      : matlab
categories : [math]
tags       : [notes]
---

### 资料
- [官方自带教程](https://cn.mathworks.com/help/matlab/getting-started-with-matlab.html)
- [Andrew N.G machine learning matlab tutorial](https://www.coursera.org/learn/machine-learning/resources/QQx8l)

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

#### matrix
```
zeros
ones
rand
randn
eye
>> A = [1,2;3,4;5,6]

A =

     1     2
     3     4
     5     6

>> A([1 3],:) % 第一行和第三行

ans =

     1     2
     5     6

>> A(:) % 所有元素 一列

ans =

     1
     3
     5
     2
     4
     6

>> A = [A;[7 8]] % 追加行

A =

     1     2
     3     4
     5     6
     7     8

>> A = [A, [12;13;14;16]] % 追加列

A =

     1     2    12
     3     4    13
     5     6    14
     7     8    16

```
`* .*`  % multiply
`A'` % transpose
`pinv(A)` % inverse
`[r,c] = find(A<3)` % location of elements that < 3
`prob(A)` % production
 `ceil(A)` % round
`max(A,[],1)` % first dimension
`flipud(A,1)` % flip up down

### plot
```
plot
hold on;
xlabel
ylabel
legent
title
axis([0.5 1 -1 1])
print -dpdg 'jj.png'
figure(1); plot(t,y1);
subplot(1,2,1);
imagesc(magic(15)), colorbar, colormap gray;
```

### control statement 
```
for i = 1:10,
  disp(i);
end

if ,
elseif ,
else ,
end;
```

