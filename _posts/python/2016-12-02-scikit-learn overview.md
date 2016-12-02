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

 











