"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
a = input("text off to exit")
abc = {}
while a != "off":
    start = input("begin?")
    start.lower
    if start == "yes":
        chart = input()
        singer = input()
        track = input()
    else:
        break
    abc[chart, singer] = track
    print(abc)

