# 完整函式

def func(x):
    return  x ** 2

#區間 [0,2]分成4個子區間
num_intervals = 4
delta_x = 2 / num_intervals

#計算舉行面積
area = 0

for i  in range(num_intervals):
    #計算每個小區間的左端點和右端點
    left_x = i * delta_x
    right_x = (i+1) * delta_x

    #計算舉行面積與累計
    area += delta_x * func(left_x)

#輸出面積

print(f"近似面積：{area}")

