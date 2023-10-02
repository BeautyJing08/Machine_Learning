import matplotlib.pyplot as plt
import numpy as np

print("M11105102 王菁")

def f(x):  # 宣告題目的圖形

    return x ** 2


# 寫出起始點與終點
start = 0
end = 2

# 定義區分的塊數
n = 4 #切幾份=n值
dx = (end - start) / n  # 每塊x的寬度

area = 0  # 初始化面積=0

# 繪製圖面
x = np.linspace(-2, 4, 100)  # 生成100個點 -2~4之間的x點 (-2~4之間生成100個點) #越多線越滑順
y = f(x)
plt.plot(x, y, 'r', linewidth=1, label='y = x^2')  # x,y點
plt.grid(True) #顯示格線
# 計算面積


for i in range(n +1):  # 結尾的那一次也計算
    xi = start + dx * i
    print(f"xi= {xi}")
    yi = f(xi)
    print(f"yi= {yi}")
    print(f"old area = {area}")
    area += yi * dx
    print(f"new area = {area}")
    rect = plt.Rectangle((xi, 0), dx, yi, color='b', alpha=0.3)
    plt.gca().add_patch(rect)

print(f"總面積為:{area}")
plt.scatter(2, 4, color='blue', label='Point (2, 4)')

plt.xlabel('x') #設定水平標
plt.ylabel('y') #設定垂直標
plt.legend()
plt.title('y = x^2') # 設定標題

plt.show()




###################################### 自己計算part ######################################

#
# x0 = 0
# y0 = f(x0)
# area0 = y0* dx
# print(f"x0={x0}, y0={y0}, area0={area0}")
#
# x1 = 0.5
# y1 = f(x1)
# area1 = y1 * dx
# print(f"x1={x1}, y1={y1}, area1={area1}")
#
# x2 = 1.0
# y2 = f(x2)
# area2 = y2 * dx
# print(f"x2={x2}, y2={y2}, area2={area2}")
#
# x3 = 1.5
# y3 = f(x3)
# area3 = y3 * dx
# print(f"x3={x3}, y3={y3}, area3={area3}")
#
# x4 = 2.0
# y4 = f(x4)
# area4 = y4 * dx
# print(f"x4={x4}, y4={y4}, area4={area4}")
# print(f"from 0 to 2 's area is = {area0+area1+area2+area3+area4}")

# print(range(n))