# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:14:17 2023

@author: user
"""

# In[]: decision tree for regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv('D:\petrol_consumption.csv')
dataset.head()
dataset.describe(percentiles=None, include=None, exclude=None)

X = dataset.drop('Petrol_Consumption', axis=1)
y = dataset['Petrol_Consumption']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

df=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})


from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

a = dataset.describe()

# In[]: decision tree for classification

# %matplotlib inline
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
iris = datasets.load_iris()
x = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print("target_names: "+str(iris['target_names']))
y = pd.DataFrame(iris['target'], columns=['target'])
iris_data = pd.concat([x,y], axis=1)
#iris_data = iris_data[['sepal length (cm)','petal length (cm)','target']]
#iris_data = iris_data[iris_data['target'].isin([0,1])]
iris_data.head(3)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_data[['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']], iris_data[['target']],         
    test_size=0.3, random_state=0)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion = 'entropy', random_state=0)
#iris_data['target_class'] = iris_data['target_name'].map(target_class)
clf.fit(X_train,y_train)
clf.predict(X_train)

clf.predict(X_train.iloc[0:1,:])
