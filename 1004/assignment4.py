import os
import pandas as pd
print("M11105102 王菁 HW4")
print("寫出一個function，讀取資料表，把兩筆Open最大值資料挑出來並刪除 ")

# regr = linear_model.LinearRegression()  # 從sklearn中拿出linear_model (線性回歸模型) (一個空的線性回歸模型)

# data = pd.read_csv('D:\\Google_Stock_Price_Train.csv')
cwd = os.getcwd()
file_path = rf"{cwd}\Google_Stock_Price_Train.csv"
df = pd.read_csv(file_path)  # 讀取資料
print("=============印出原始資料表 df ========================")
print(df)  # 會看到df資料表是原始資料表，擁有Date、Open、High、Low、Close、Volume欄位

# print("========== 印出 只拿出561筆資料的原始資料表 要來訓練模型 =================")
# train = df.iloc[0:561, :]  # 設定一個train 資料表，是從df拿561筆內容
# print(train)

train = df.iloc[0:561, :]  # 設定一個train 資料表，是從df拿561筆內容


# def readStockPriceCSV(Open, Close, Num):
#     print(Open)
#     return
#
# readStockPriceCSV(train[['Open']] ,train[['Close']], 2 )

def readStockPriceCSVWithTime(df, StartDate, EndDate, Num):
    print("===========印出filter_df===============")
    df.loc[:, 'Date'] = pd.to_datetime(df['Date'])  # 把資料表內的Date欄，改成DateTime型別
    #
    StartDate = pd.to_datetime(StartDate) #新設一個新的欄位資料名叫做StartDate
    EndDate = pd.to_datetime(EndDate) #新設一個新的欄未資料名叫做EndDate

    filter_df = df[(df['Date'] >= StartDate) & (df['Date'] <= EndDate)] #此資料夾內大於開始時間 且 小於結束時間的被抓出來
    print(filter_df)

    BiggestOpenPriceRow_index = filter_df['Open'].nlargest(Num).index #這個filter_df內，Open欄，最大的兩個值(Num是有幾個值被抓出來)，.index是那些被抓出來的位置
    BiggestOpenPriceRow_rows = filter_df.loc[BiggestOpenPriceRow_index] #把index丟到filter_df內，可以得到那一整列的資料

    filter_df = filter_df.drop(index=BiggestOpenPriceRow_index) #filter_df把這個最大的值去掉
    print("最大的兩列是")
    print(BiggestOpenPriceRow_rows)

    print("刪除兩列後的資料表")
    print(filter_df)
    return


filter_df = readStockPriceCSVWithTime(train, '2012-01-06', '2012-01-15', 2)
