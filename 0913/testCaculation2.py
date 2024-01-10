n = 0
stopNum = 15

a_values = []  # 用於保存每輪的 a 值
b_values = []  # 用於保存每輪的 b 值
result_values = []  # 用於保存每輪的 result 值

a = 0
b = 0

while n < stopNum:
    print(f"it's {n} iteration")
    n += 1
    result = a + b

    # 將每一輪的值保存到列表中
    a_values.append(a)
    b_values.append(b)
    result_values.append(result)

    print(f"a={a}, b={b}, a+b = result = {result}")

    if a < 5:
        a += 1
    elif a == 5:
        b += 1

    if result == 10:
        print("已完成運算")
        break

# 輸出資料表
print("\n資料表:")
print("  a  |  b  |  result")
print("--------------------")
for i in range(len(a_values)):
    print(f" {a_values[i]:<4}| {b_values[i]:<4}| {result_values[i]:<6}")