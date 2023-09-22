from sklearn import linear_model
import pandas as pd


size=[5,10,12,14,18,30,33,55,65,80,100,150]
distance=[50,20,70,100,200,150,30,50,70,35,40,20]
price=[300,400,450,800,1200,1400,2000,2500,2800,3000,3500,9000]

series_dict={'X1':size,'X2':distance,'y':price} #設定欄位名稱為 "key name" : "value", 設定字典
df=pd.DataFrame(series_dict) #使用pandas的功能DateFrame 設定資料表


print("============== it's df =====================")
print(f"df's shape = {df.shape}, df's row = {df.shape[0]}, df's col = {df.shape[1]}")
print(df) #印出此data的表(dataFrame)

train = df.iloc[0:10,:] #df.iloc[第0行~第10行, 全部的列]

print("============ it's train df.iloc[0:10,:]===============================")
print(train)
print("現在把train dataFrame拆程兩個資料表，分別稱X(包含X1&X2欄位) & y (包含y欄位)")

X = train[['X1','X2']] # X變數 是 一個新的資料表名叫X，內容為train內的 "X1" 欄位 & "X2"欄位
y = train[['y']] # y變數 是把

print(X)
print("=====")
print(y)

print("===========================================")
#test = df.iloc[10:,:]
#X_test = test[['X1','X2']]
#y_test = test[['y']]


#X_test = df.iloc[10:,:]
#y_test = df.iloc[0:10,:]

regr=linear_model.LinearRegression() #現在設定一個變數名叫做regr , 是要開啟 sklearn 的 linear_model 套件，中的 LinearRegression()。開啟一個新的線性回歸模型 (空白模型)
regr.fit(X, y) #把這個線性回歸模型，裝入X資料表 與 y資料表，進行一件事情，就是使用X資料表中的X1&X2 來預測y值 ###也就是把模型給訓練好
regr.predict(X) #把X資料表再丟進去一次這個已經訓練好的線性模型，預測出自己的答案
print("進行第一次的X預測")
print(regr.predict(X))

regr.coef_ #此句程式碼，是來說明這個線性模型的 權重(Weight) or 斜率(Slope)
print("印出此線性模型的 權重(Weight) or 斜率(Slope)")
print(regr.coef_)
print("===================")


prediction = pd.DataFrame(regr.predict(X),columns=['Prediction']) #創建一個新的資料表名叫做prediction，欄位名稱叫做"Prediction"，內容為線性回歸，把X資料表丟進去得到的 預測
print("印出prediction資料表")
print(prediction)

comparison_table = pd.concat([prediction,y],axis = 1) #創建一個新的資料表，名叫做comparison_table ， 放prediction欄位與原本題目提供的y值欄位做比較(放在同一張資料表) #axis=1 == y資料表會插在prediction的右邊新"欄位" (column)
print("印出comparison_table 資料表")
print(comparison_table)


print("現在要把Error(殘差)計算出來，並且放在comparison_table")
comparison_table['Error'] = comparison_table.Prediction - comparison_table.y #創建一個新欄位名叫做"Error"，讓Prediction - y 值 (預測值 - 題目y)
print(comparison_table)


