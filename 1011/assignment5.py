import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

print("~~ Machine Learning Homework05 ~~")
print("M1105102 王菁")

### STEP 01 : 讀取資料表 ####
cwd = os.getcwd()
file_path = rf"{cwd}\Google_Stock_Price_Train.csv"
data = pd.read_csv(file_path)

print("==========我是原始資料表==================")
print(data)  # 印出資料表
print("=========================================")
print("印出561筆open資料")
### STEP 02 : 處理資料表的open出來 ####

data_open = data[['Open']] #用雙括號的話，就會有欄位名稱 #從data中，拿出open的資料
data_open = data_open.iloc[0:561, :] #從data_open當中，拿出561筆資料
print(data_open)
print("=========================================")
print("印出斜率")


cut_size = 5 #切割的尺寸是每五個一個尺寸
slopes = [] #放斜率的array

# for i in range(0, 100 , cut_size): #從0開始，終點是100(不含100)，每幾個分割一次
#     print(i)

########################################

for i in range(0, len(data_open) - cut_size + 1 , cut_size):
    model = LinearRegression() #空白模型
    X = np.arange(cut_size).reshape(-1,1) #創造一個從[0~cut_size]的陣列，此處就會變成[0,1,2,3,4]，但使用numpy的reshape功能，會變成二微陣列，變成[[0],[1],[2],[3],[4]]
    y = data_open[i:i+cut_size] #第一筆資料是data_open[0:0+5] == [0:5] = [0],[1],[2],[3],[4] #就是從data_open拿出前五筆資料
    model.fit(X,y) #將模型調教好，用(X,y)來畫出線性回歸模型
    slope = model.coef_[0] #slope 為 模型的斜率
    slopes.append(slope[0]) #將slope(斜率) 插進 slopes的array當中

print("斜率array=")
print(slopes) #印出斜率