list1 =[]
while True:
    prepod = input("введи имя препода - ")
    if prepod != "0":
        if prepod not in list1:
            list1.append(prepod)
            print("препод добавлен")
        else:
            print("препод уже есть")

    else:
        print("Thanks for game")
        break
list1.sort()
print(list1)

