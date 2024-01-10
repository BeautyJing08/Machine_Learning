a = 0
b = 0
n = 1
while True:
    print(f"a= {a} , b= {b} , it's {n} iteration")
    result = a + b
    n += 1
    print(f"a + b 的值: {result}")
    print()


    if a < 5:
        a += 1

    elif a == 5:
        b += 1

    if result == 8:
        print("已完成運算")
        break
