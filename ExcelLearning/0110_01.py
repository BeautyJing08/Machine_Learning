#### 使用 openpyxl套件 ####
import openpyxl
# 開啟現有的Excel文件
workbook = openpyxl.load_workbook("0110test.xlsx") #打開excel資料表
sheet = workbook.active #預設第一個資料表

# 確認欄位名稱
column_names = [cell.value for cell in sheet[1]]

if "a" not in column_names or "b" not in column_names or "result" not in column_names:
    print("Excel文件的欄位名稱不正確，請檢查。")
    # 可以根據需要進一步處理錯誤或退出程式

# 確認最後一筆資料的位置
last_row = sheet.max_row
print(last_row)