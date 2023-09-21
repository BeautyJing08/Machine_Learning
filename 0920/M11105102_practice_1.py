# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 01:05:33 2023

@author: user
"""
################ M11105102 王菁 #########################
print("M11105102 王菁")
import pandas as pd
import numpy as np
import os
# print(pd.__version__) #印出 pandas version

### STEP 01 : 讀取資料表 ####
# file_path = r"D:\OneDrive\OneDrive - 國立臺灣科技大學\A SI5032701 機器學習\0913 - week02\20230913_machine_learning\M11105102_assignment.csv"
cwd = os.getcwd()
file_path = rf"{cwd}\M11105102_assignment.csv"
data = pd.read_csv(file_path)

print("==========我是原始資料表==================")
print(data)  # 印出資料表
print("=========================================")
# i=5
# print(data.loc[i,'type'])
# print(data.loc[7,'score'])

### STEP 02 : 判斷csv檔案的內容中，成績是否會有空值的區域，若有空值，則讓當前欄未讀取上方欄位的值
for i in range(0, len(data)):
    if pd.isna(data.loc[i, 'score']):  # 用pandas的功能查詢欄位是否為空值
        data.loc[i, 'score'] = data.loc[i - 1, 'score']  # 讓空的那個值，讀取上一欄位的值

print("==========我是填完空值的資料表==============")
print(data)  # 印出修改後的資料表
print("==========================================")
### STEP 03 : 增加一個新的欄位叫做 "revise" ， 為調整成積後的欄位

for i in range(0, len(data)):
    if data.loc[i, 'type'] == "A": #若type是A，score+5放在"revise"欄位內
        data.loc[i, 'revise'] = data.loc[i, 'score'] + 5
    elif data.loc[i, 'type'] == "B":
        data.loc[i, 'revise'] = data.loc[i, 'score'] + 3

    elif data.loc[i,'revise'] >= 100: #如果revise的答案>=100的話，滿分是100，不能超過100
        data.loc[i,'revise'] ==100
    else:
        data.loc[i, 'revise'] = data.loc[i, 'score']

### STEP 04 : 增加一個欄位叫做"Grade" 來寫說學生是Pass or Fail
data['Grade'] = [''] * len(data) #創建一個新欄位名叫做Grade，並且列數為 len(data) 這樣資料表的尺寸才會正確 *** 同時設定了"Grade"是字串欄位
# print(data['Grade'].dtype) #查看"Grade"的資料型別，字串是object
# data['Grade'] = data['Grade'].astype(str) #將data['Grade']的資料欄位，全部修改為"字串"型別(astype(str))

# data['Grade'] = 0
# print(data['Grade'].dtype) #此兩句是

for i in range(0, len(data)):
    if data.loc[i, 'revise'] >= 60 :
        data.loc[i, 'Grade'] = "Pass"
    else :
        data.loc[i, 'Grade'] = "Fail"


print("==========我是有更新成績&是否及格的資料表=============")
print(data)
