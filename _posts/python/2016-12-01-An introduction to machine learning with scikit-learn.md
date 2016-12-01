---
layout     : post
title      : An introduction to machine learning with scikit-learn
categories : [python]
tags       : [notes]
---

## Machine learning: the problem setting

### supervised learning

#### classfication

#### regression

### unsupervised learning

## Loading an example dataset

- [python加载数据的方法汇总](http://www.cuizixin.top/blog/2016/11/22/python%E5%8A%A0%E8%BD%BD%E6%95%B0%E6%8D%AE%E7%9A%84%E6%96%B9%E6%B3%95%E6%B1%87%E6%80%BB.html)

## learning and predicting

### Choosing the parameters of the model

#### grid search 

#### cross validation

## model persistence

### pickle

## conventions

### type casting 

- Unless otherwise specified, input will be cast to float64: 除非另有指定，否则输入类型指定为float64
- Regression targets are cast to float64, classification targets are maintained: 

### refitting and updating parameters

#### hyper-parameter 
[超参数](https://www.quora.com/What-are-hyperparameters-in-machine-learning): 不能通过常规训练学习到参数（比如学习速率，树的深度，基学习器类型等），需要我们额外指定，一般是训练前就指定好。
