---
layout     : post
title      : scikit-learn overview
categories : [python]
tags       : [notes]
---

- [scikit-learn 使用总结](http://python.jobbole.com/86910/#comment-94232)

## scikit-learn 基础介绍

### estimator 估计器

- `fit()`

- `predict()`

### transformer 转换器

- `fit()`

- `transform()`

- `fit_transform()`

### pipeline 流水线

`sklearn.pipeline`

#### 功能

- 跟踪记录各个步骤的操作（以方便地重现实验结果）
- 对各步骤进行一个封装
- 确保代码的复杂程度不至于超出掌控范围

#### 基本使用方法
流水线的输入为一连串的数据挖掘步骤，其中最后一步必须是`estimator`，前几步是`transformer`。前一步的输出是下一步的输入，数据集先经过几个`transformer`，最后到达`estimator`通过机器学习建立预测模型。<br>
一个流水线例子：

```python
scaling_pipeline = Pipeline([
  ('scale', MinMaxScaler()),
  ('predict', KNeighborsClassifier())
])
```

#### 预处理

`sklearn.preprocessing`

##### 规范化：
- `MinMaxScaler`: 最大最小值规范化
- `Normalizer`: 使每条数据各特征值的和为1
- `StandardScaler`: 为使各特征值的均值为0，方差为1

##### 编码
- `LabelEncoder`: 把字符串类型的数据转化为整型
- `OneHotEncoder`: 特征用一个二进制数字来表示
- `Binarizer`: 为将数值型特征二值化
- `MultiLabelBinarizer`: 多标签二值化

### 特征

#### 特征抽取

`sklearn.feature_extraction`

- DictVectorizer： 将dict类型的list数据，转换成numpy array

```python
>>> measurements = [
...     {'city': 'Dubai', 'temperature': 33.},
...     {'city': 'London', 'temperature': 12.},
...     {'city': 'San Fransisco', 'temperature': 18.},
... ]

>>> from sklearn.feature_extraction import DictVectorizer
>>> vec = DictVectorizer()

>>> vec.fit_transform(measurements).toarray()
array([[  1.,   0.,   0.,  33.],
       [  0.,   1.,   0.,  12.],
       [  0.,   0.,   1.,  18.]])

>>> vec.get_feature_names()
['city=Dubai', 'city=London', 'city=San Fransisco', 'temperature']
```

- FeatureHasher ： 特征哈希，相当于一种降维技巧
- image：图像相关的特征抽取
- text： 文本相关的特征抽取
 - text.CountVectorizer：将文本转换为每个词出现的个数的向量
 - text.TfidfVectorizer：将文本转换为tfidf值的向量
 - text.HashingVectorizer：文本的特征哈希

#### 特征选择

`sklearn.feature_selection`

##### 为什么要特征选择
1. 降低复杂度
2. 降低噪音
3. 降低模型可读性

- VarianceThreshold： 删除特征值的方差达不到最低标准的特征
- SelectKBest： 返回k个最佳特征
- SelectPercentile： 返回表现最佳的前r%个特征
<br>

单个特征和某一类别之间相关性的计算方法有很多。最常用的有卡方检验（χ2）。其他方法还有互信息和信息熵。
- chi2: 卡方校验

### 降维

`sklearn.decomposition`

- 主成分分析算法（principal component analysis, PCA）
目的是找到能用较少信息描述数据集的特征组合。

### 集成学习

`sklearn.ensemble `

- BaggingClassifier： Bagging分类器组合
- BaggingRegressor： Bagging回归器组合
- AdaBoostClassifier： AdaBoost分类器组合
- AdaBoostRegressor： AdaBoost回归器组合
- GradientBoostingClassifier：GradientBoosting分类器组合
- GradientBoostingRegressor： GradientBoosting回归器组合
- ExtraTreeClassifier：ExtraTree分类器组合
- ExtraTreeRegressor： ExtraTree回归器组合
- RandomTreeClassifier：随机森林分类器组合
- RandomTreeRegressor： 随机森林回归器组合

#### 分类

##### bagging

##### boosting

### 模型评估（度量）

`sklearn.metrics`<br>
包含评分方法、性能度量、成对度量和距离计算

#### 分类结果度量

- accuracy_score：分类准确度
- condusion_matrix ：分类混淆矩阵
- classification_report：分类报告
- precision_recall_fscore_support：计算精确度、召回率、f、支持率
- jaccard_similarity_score：计算jcaard相似度
- hamming_loss：计算汉明损失
- zero_one_loss：0-1损失
- hinge_loss：计算hinge损失
- log_loss：计算log损失

#### 回归结果度量

- explained_varicance_score：可解释方差的回归评分函数
- mean_absolute_error：平均绝对误差
- mean_squared_error：平均平方误差

#### 多标签的度量

- coverage_error：涵盖误差
- label_ranking_average_precision_score：计算基于排名的平均误差Label ranking average precision (LRAP)

#### 聚类的度量

- adjusted_mutual_info_score：调整的互信息评分
- silhouette_score：所有样本的轮廓系数的平均值
- silhouette_sample：所有样本的轮廓系数

### 交叉验证

`sklearn.cross_validation`

- KFold：K-Fold交叉验证迭代器。接收元素个数、fold数、是否清洗
- LeaveOneOut：LeaveOneOut交叉验证迭代器
- LeavePOut：LeavePOut交叉验证迭代器
- LeaveOneLableOut：LeaveOneLableOut交叉验证迭代器
- LeavePLabelOut：LeavePLabelOut交叉验证迭代器
<br>
LeaveOneOut(n) 相当于 KFold(n, n_folds=n) 相当于LeavePOut(n, p=1)。
LeaveP和LeaveOne差别在于leave的个数，也就是测试集的尺寸。LeavePLabel和LeaveOneLabel差别在于leave的Label的种类的个数。
LeavePLabel这种设计是针对可能存在第三方的Label，比如我们的数据是一些季度的数据。那么很自然的一个想法就是把1,2,3个季度的数据当做训练集，第4个季度的数据当做测试集。这个时候只要输入每个样本对应的季度Label，就可以实现这样的功能。
以下是实验代码，尽量自己多实验去理解。

```python
#coding=utf-8
import numpy as np
import sklearnfrom sklearn
import cross_validation
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8],[9, 10]])
y = np.array([1, 2, 1, 2, 3])
def show_cross_val(method):    
  if method == "lolo":        
    labels = np.array(["summer", "winter", "summer", "winter", "spring"])        
    cv = cross_validation.LeaveOneLabelOut(labels)          
  elif method == 'lplo':        
    labels = np.array(["summer", "winter", "summer", "winter", "spring"])        
    cv = cross_validation.LeavePLabelOut(labels,p=2)    
  elif method == 'loo':        
    cv = cross_validation.LeaveOneOut(n=len(y))    
  elif method == 'lpo':        
    cv = cross_validation.LeavePOut(n=len(y),p=3)    
  for train_index, test_index in cv:        
    print("TRAIN:", train_index, "TEST:", test_index)        
    X_train, X_test = X[train_index], X[test_index]        
    y_train, y_test = y[train_index], y[test_index]        
    print "X_train: ",X_train        
    print "y_train: ", y_train        
    print "X_test: ",X_test        
    print "y_test: ",y_test
if __name__ == '__main__':    
  show_cross_val("lpo")
```

#### 常用方法

- train_test_split：分离训练集和测试集（不是K-Fold）
- cross_val_score：交叉验证评分，可以指认cv为上面的类的实例
- cross_val_predict：交叉验证的预测。

### 网格搜索

`sklearn.grid_search`

- GridSearchCV：搜索指定参数网格中的最佳参数
- ParameterGrid：参数网格
- ParameterSampler：用给定分布生成参数的生成器
- RandomizedSearchCV：超参的随机搜索
通过best_estimator_.get_params()方法，获取最佳参数。

### 多分类、多标签分类

`sklearn.multiclass`

## 具体模型

### 朴素贝叶斯

## scikit-learn扩展

### 概览

### 创建自己的转换器
