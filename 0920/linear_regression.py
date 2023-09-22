# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:04:44 2020

@author: Stanley
"""
# In[] linear regression
from sklearn import linear_model
import pandas as pd
import sklearn

import statsmodels.api as sm
import numpy as np
import os

# regr=linear_model.LinearRegression() #從sklearn中拿出linear_model (線性回歸模型)
#
# # data = pd.read_csv('D:\\Google_Stock_Price_Train.csv')
# cwd = os.getcwd()
# file_path = rf"{cwd}\M11105102_Google_Stock_Price_Train.csv"
# data = pd.read_csv(file_path) #讀取資料
#
# print(data)
#
#
# X = data[['Open','High','Low']]
# y = data[['Close']]
#
# X2 = sm.add_constant(X)
#
# est = sm.OLS(y,X)
# est = sm.OLS(y,X2)
# est2 = est.fit()
# print(est2.summary())
# data.cov(min_periods=12)
#==================================================================================#
#==================================================================================#
#==================================================================================#
#==================================================================================#
#==================================================================================#
# In[]:
import pandas as pd
import sklearn


size=[5,10,12,14,18,30,33,55,65,80,100,150]
distance=[50,20,70,100,200,150,30,50,70,35,40,20]
price=[300,400,450,800,1200,1400,2000,2500,2800,3000,3500,9000]

series_dict={'X1':size,'X2':distance,'y':price}
df=pd.DataFrame(series_dict)

train = df.iloc[0:10,:]
X = train[['X1','X2']]
y = train[['y']]


#test = df.iloc[10:,:]
#X_test = test[['X1','X2']]
#y_test = test[['y']]


#X_test = df.iloc[10:,:]
#y_test = df.iloc[0:10,:]

regr=linear_model.LinearRegression()
regr.fit(X, y)
regr.predict(X)


regr.coef_


prediction = pd.DataFrame(regr.predict(X),columns=['Prediction'])
comparison_table = pd.concat([prediction,y],axis = 1)
comparison_table['Error'] = comparison_table.Prediction - comparison_table.y

print(prediction)
#==================================================================================#
#==================================================================================#
#==================================================================================#
#==================================================================================#
#==================================================================================#
#
# import statsmodels.api as sm
# import scipy.stats as stats
# from matplotlib import pyplot as plt
#
# res = comparison_table['Error']
# fig = sm.qqplot(res,stats.t, fit=True, line="45")
# plt.show()
#
# stats.shapiro(res)
#
#
#
# #######################################
#
# X = df[['X1','X2']]
#
# #X = df[['X1']]
#
# y = df[['y']]
#
# X2 = sm.add_constant(X)
#
# est = sm.OLS(y,X2)
# est2 = est.fit()
# print(est2.summary())
#
#
