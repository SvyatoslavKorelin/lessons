"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def IMT():
    weight = int(input("введите вес"))
    height = int(input("введите рост"))
    b = height **2
    a = weight/b
    return a


def IMT_Count(a):
    if a < 18.5:
        print("недостаточный вес")
    elif a >= 18.5 and a <= 25:
        print("нормальный вес")
    elif a >25:
        print("избыточный вес")


IMT_Count(IMT())
