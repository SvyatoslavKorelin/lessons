"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».
Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""
def points_count(points):
    if points <= 49:
        print("скидка 10%")
    elif points >= 50 and points <= 99:
        print("скидка 15%")
    elif points >= 100:
        print("скидка 20 %")


points = int(input('kolvo ballov '))
points_count(points)