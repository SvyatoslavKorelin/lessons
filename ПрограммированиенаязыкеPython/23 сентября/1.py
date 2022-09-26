list1 =[]
while True:
    game = input("введи названеи игры - ")
    if game != "0":
        if game not in list1:
            list1.append(game)
            print("игра добавлена")
        else:
            print("игра в наличии")
    else:
        print("Thanks for game")
        break
list1.sort()
print(list1)
