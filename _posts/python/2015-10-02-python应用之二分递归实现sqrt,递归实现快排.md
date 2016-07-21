---
layout     : post
title      : python应用2之二分递归实现sqrt,递归实现快排
categories : [python]
tags       : [notes]
---
```python
def sqrt(x,min=0,max=0):
    if max==0:
        max = x
    mid = (max+min)/2
    if abs(mid**2-x)<0.000000000000000000000000000000000000000000001:
        return mid
    elif mid**2<x:
        return sqrt(x,mid,max)
    elif mid**2>x:
        return sqrt(x,min,mid)
print(sqrt(36))
```
```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def partition(list,p,r):
    i = p-1
    for j in range(p,r):
        if list[j]<list[r]:
            i+=1
            list[j],list[i] = list[i],list[j]
    list[i+1],list[r] = list[r],list[i+1]
    return i+1
def quickSort(list,p=0,r=-100):
    #print(list)
    if r == -100:
        r = len(list)-1
    if p>=r:
        return
    q = partition(list,p,r)
    quickSort(list,p,q-1)
    quickSort(list,q+1,r)
l = [2,3,4,1,5,6,3,8,0,12]
quickSort(l)
print(l)
```