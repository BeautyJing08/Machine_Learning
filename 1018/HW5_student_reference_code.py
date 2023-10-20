import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import os

print("M11105102 王菁")
print("Assignment 10")

cwd = os.getcwd()
file_path = rf"{cwd}\Google_Stock_Price_Train.csv"
df = pd.read_csv(file_path)


# df = pd.read_csv("C:/homework/Google_Stock_Price_Train.csv")
df["Date"] = pd.to_datetime(df["Date"]) #把df內的date欄位，改成datetime型別
df = df.sort_values(by="Date") #用date來排序資料


slopes = [] #擺放斜率的array

def drawSlopeDiagramWithWindowSize(window_size,stride,k, slopes): #windows_size==幾筆成為一個資料；stride==每一段移動的距離；k==幾倍標準差
    OriginalStide= stride
    for stride in range(0, len(df), window_size):  # 讓i從0開始，到df資料結束，每幾筆資料切成一刀
        if stride + window_size < len(df):  # 如果i + 幾筆資料 會<總比數，則進行下列程式碼；若i+資料>總比數，直接終止迴圈
            data_subset = df[ stride: stride + window_size]  # 拿出資料(y值) #第一筆資料是df[0:0+5] == [0:5] = [0],[1],[2],[3],[4] #就是從df拿出前五筆資料

            model = LinearRegression()
            # model(X,y) X=df的數量改成二維陣列e.g.[[0],[1],[2],[3],[4]] ； y的值就是data_subset取出的資料
            model.fit(
                np.arange(len(data_subset)).reshape(-1, 1),
                data_subset["Open"].values.reshape(-1, 1),
            )

            slope = model.coef_[0][0]  # 斜率
            slopes.append(slope)
    outOfControl_Num = sum(1 for element in slopes if (element > np.mean(slopes)+ k * np.std(slopes)) or (element < np.mean(slopes) - k * np.std(slopes)))
    # print(f"all slopes= {slopes}")


    # print(f"今天windows size= {window_size}, stride= {OriginalStide}, k={k}時")
    # print(f"平均數Mean= {np.mean(slopes)}, 一倍標準差std= {np.std(slopes)}")
    # print(f"OOC(out of Control)數量= {outOfControl_Num}")
    # print(f"OOC rate= {outOfControl_Num / len(slopes)}")

    mean = np.mean(slopes)
    std = np.std(slopes)
    ooc = outOfControl_Num
    ooc_rate = ooc / len(slopes)

    print(f"今天 windows size= {window_size}, stride= {OriginalStide}, k={k}時")
    print(f"平均數 Mean= {mean}, 一倍標準差 std= {std}")
    print(f"OOC(out of Control)數量= {ooc}")
    print(f"OOC rate= {ooc_rate}")
    ## 開始畫圖 ##
    plt.figure(figsize=(12, 6))  # 設定圖片尺寸
    plt.plot(slopes, marker="o", linestyle="-")  # 把每一個斜率的點畫出一個點
    plt.axhline(np.mean(slopes), color="red", linestyle="--", label="mean ")  # 畫出平均值
    plt.axhline(
        np.mean(slopes) + k * np.std(slopes),
        color="green",
        linestyle="--",
        label=f"upper bound, with {k} std",
    )  # 畫出平均值 + k倍標準差
    plt.axhline(
        np.mean(slopes) - k * np.std(slopes),
        color="green",
        linestyle="--",
        label=f"lower bound, with {k} std",
    )  # 畫出平均值 - k倍標準差
    plt.xlabel("time")  # x軸是時間
    plt.ylabel("slop")  # y軸是斜率
    plt.title("control chart")
    plt.legend()
    plt.show()
    print()
    return mean, std, ooc, ooc_rate, k


# drawSlopeDiagramWithWindowSize(5,1,3) #使用function
mean,std, ooc, ooc_rate, k =  drawSlopeDiagramWithWindowSize(window_size=5, stride=1, k=3, slopes=slopes) #window size=5, stride=1, k倍標準差
# mean,std, ooc, ooc_rate, k =  drawSlopeDiagramWithWindowSize(window_size=5, stride=1, k=4, slopes=slopes) #window size=5, stride=1, k倍標準差

###############################################################
k_arr = [1,2,3,4,5]

dataTable = pd.DataFrame(columns=["Mean", "Std", "k", "OCC", "OCC_rate"])

for i in k_arr:
    slopes=[] #每次放進去的slopes都是一個新的空array
    mean, std , occ, occ_rate, k = drawSlopeDiagramWithWindowSize(window_size=5, stride=1, k=i, slopes=slopes)
    data = {"Mean": mean, "std": std, "k":k, "OCC":occ, "OCC_rate":occ_rate }
    dataTable.loc[len(dataTable)] = data

print(dataTable)