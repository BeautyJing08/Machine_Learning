from sklearn import linear_model
import pandas as pd
import sklearn

import statsmodels.api as sm  # 這個目前還不知道功能
import numpy as np
import os

regr = linear_model.LinearRegression()  # 從sklearn中拿出linear_model (線性回歸模型) (一個空的線性回歸模型)

# data = pd.read_csv('D:\\Google_Stock_Price_Train.csv')
cwd = os.getcwd()
file_path = rf"{cwd}\M11105102_Google_Stock_Price_Train.csv"
df = pd.read_csv(file_path)  # 讀取資料
print("=============印出原始資料表 df ========================")
print(df)  # 會看到df資料表是原始資料表，擁有Date、Open、High、Low、Close、Volume欄位

print("========== 印出 只拿出561筆資料的原始資料表 要來訓練模型 =================")
train = df.iloc[0:561, :]  # 設定一個train 資料表，是從df拿561筆內容
print(train)

X = train[['Open']]  # X變數 是 創建一個新的資料表名叫X，內容為train內的 "Open" 欄位
y = train[['Close']]  # y變數 是 創建一個新的資料表名叫y，內容為train內的 "Close" 欄位

# print("印出訓練的 X資料表與 y資料表")
# print(X)
# print(y)

regr = linear_model.LinearRegression()  # 現在設定一個變數名叫做regr , 是要開啟 sklearn 的 linear_model 套件，中的 LinearRegression()。開啟一個新的線性回歸模型 (空白模型)
regr.fit(X, y)  # 訓練模型 #把這個線性回歸模型，裝入X資料表 與 y資料表，進行一件事情，就是使用X資料表中的"Open" 來預測"Close"值 ###也就是把模型給訓練好
regr.predict(X)  # 把X資料表再丟進去一次這個已經訓練好的線性模型，預測出自己的答案

regr.coef_  # 此句程式碼，是來說明這個線性模型的 權重(Weight) or 斜率(Slope)
print("此561筆資料表所算出來的權重值為 : 印出此線性模型的 權重(Weight) or 斜率(Slope)")
print(regr.coef_)

################### 畫圖看open與close的關係(訓練模型的圖)#######################
# import matplotlib.pyplot as plt
#
# # 创建一个散点图
# plt.scatter(X, y, c='b', marker='o', label='Scatter Plot')
#
# # 添加轴标签和图例
# plt.xlabel('X (Open)')
# plt.ylabel('y (Close)')
# plt.legend()
#
# plt.plot(X,regr.predict(X),color ="red", label = '回歸線')
# plt.title("561 training data's Linear regression pic")
# # 显示图表
# plt.show()

#########################################################################
#########################################################################
############## 現在要拿出561筆後的資料來做預測 ， 並且與實際值做比較 #####################


test = df.iloc[561:, :]  # 創建一個test資料表，是從df資料表中拿出561欄後的資料
X_test = test[['Open']]  # X_test資料表為，test中的Open欄
y_test = test[['Close']]  # y_test資料表為，test中的Close欄
X_test.reset_index(drop=True, inplace=True)  # 把X_test的資料表，索引重置，改成從0開始
y_test.reset_index(drop=True, inplace=True)  # 把y_test的資料表，索引重置，改成從0開始
print("====現在開始印出要測試的資料表(原資料表561行後的資料)=========")
print("")
print(X_test)
print(y_test)

prediction = pd.DataFrame(regr.predict(X_test), columns=['Prediction'])  # 創建一個新的資料表名叫做prediction，欄位名稱叫做"Prediction"，內容為線性回歸，把 X_test資料表丟進去得到的 預測
print("印出prediction資料表")
print(prediction)

comparison_table = pd.concat([prediction, y_test], axis=1)  # 創建一個新的資料表，名叫做comparison_table ， 放prediction欄位與原本題目提供的y_test值欄位做比較(放在同一張資料表) #axis=1 == y資料表會插在prediction的右邊新"欄位" (column)
print("印出comparison_table 資料表")
print(comparison_table)

print("現在要把Error(殘差)計算出來，並且放在comparison_table")
comparison_table['Error'] = comparison_table.Prediction - comparison_table.Close #創建一個新欄位名叫做"Error"，讓Prediction - y 值 (預測值 - 題目y)
print(comparison_table)

comparison_table.to_csv('comparison_table.csv')


################## 畫圖看open與close的關係(訓練模型的圖)#######################
import matplotlib.pyplot as plt

# 创建一个散点图
plt.scatter(X, y, c='b', marker='o',alpha=0.6, label='Origin dataFrame point (before 561 row')
plt.scatter(X,regr.predict(X), c='black', marker = 'o',alpha=0.6, label='use training data to prediction (before 561 row)')

plt.scatter(X_test,y_test, c="orange", marker = 'x', alpha=0.6, label = 'Origin dateFrame point (after561 row)')
plt.scatter(X_test,regr.predict(X_test), c='green', marker='x',alpha=0.6, label='prediction (after 561 row)')


# 添加轴标签和图例
plt.xlabel('(Open)')
plt.ylabel('(Close)')
plt.legend()

# plt.plot(X,regr.predict(X),color ="red", label = '回歸線')
plt.title("M11105102_Prediction_StockPrice")
# 显示图表
plt.show()