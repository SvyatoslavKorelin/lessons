price = input("цена")
time = input("время (час)")
if time >= 10:
    if time <=12:
        a = price//2
        print(a)
else:
    print(price)
