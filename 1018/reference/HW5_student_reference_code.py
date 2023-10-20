import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import os

cwd = os.getcwd()
file_path = rf"{cwd}\Google_Stock_Price_Train.csv"
df = pd.read_csv(file_path)


# df = pd.read_csv("C:/homework/Google_Stock_Price_Train.csv")
df["Date"] = pd.to_datetime(df["Date"]) #把df內的date欄位，改成datetime型別
df = df.sort_values(by="Date") #用date來排序資料


slopes = [] #擺放斜率的array


window_size = 5 #要幾筆資料來切成一刀
for i in range(0, len(df), window_size): # 讓i從0開始，到df資料結束，每幾筆資料切成一刀
    if i + window_size < len(df): #如果i + 幾筆資料 會<總比數，則進行下列程式碼；若i+資料>總比數，直接終止迴圈
        data_subset = df[i : i + window_size] #拿出資料(y值) #第一筆資料是df[0:0+5] == [0:5] = [0],[1],[2],[3],[4] #就是從df拿出前五筆資料

        model = LinearRegression()
        #model(X,y) X=df的數量改成二維陣列e.g.[[0],[1],[2],[3],[4]] ； y的值就是data_subset取出的資料
        model.fit(
            np.arange(len(data_subset)).reshape(-1, 1),
            data_subset["Open"].values.reshape(-1, 1),
        )

        slope = model.coef_[0][0] #斜率
        slopes.append(slope)
print(f"all slopes= {slopes}")

## 開始畫圖 ##
plt.figure(figsize=(12, 6)) #設定圖片尺寸
plt.plot(slopes, marker="o", linestyle="-") #把每一個斜率的點畫出一個點
plt.axhline(np.mean(slopes), color="red", linestyle="--", label="mean ") #畫出平均值
plt.axhline(
    np.mean(slopes) + 3 * np.std(slopes),
    color="green",
    linestyle="--",
    label="upper bound",
) #畫出平均值 + 三倍標準差
plt.axhline(
    np.mean(slopes) - 3 * np.std(slopes),
    color="green",
    linestyle="--",
    label="lower bound",
) #畫出平均值 - 三倍標準差
plt.xlabel("time") #x軸是時間
plt.ylabel("slop") #y軸是斜率
plt.title("control chart")
plt.legend()
plt.show()
