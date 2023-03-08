# encoding=utf-8
"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""

import multiprocessing

def information(length,width,heigh):

    square = (length * width) * heigh
    with open("information.txt","w") as f:
        f.write(str(square))


def paint():
    with open("information.txt","r+") as f:
        f.seek(0)
        square = f.read() * 5
        f.write(str = square)


if __name__  == '__main__':
    length = int(input('введи длину'))
    width = int(input('введи ширину'))
    heigh = int(input('введи высоту'))
    p1 = multiprocessing.Process(target=(information), args=(length,width,heigh))
    p2 = multiprocessing.Process(target=(paint))

    p1.start()
    p2.start()