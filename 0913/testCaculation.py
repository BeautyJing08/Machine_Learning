n = 0
stopNum = 15

a = 0
b = 0

while n < stopNum:
    print(f"it's {n} iteration")
    n += 1
    result = (a + b)
    print(f"a={a}, b={b}, a+b = result = {result} ")

    if a < 5:
        a += 1

    elif a == 5:
        b += 1

    if result == 10:
        print("已完成運算")
        break
