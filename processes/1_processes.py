# encoding=utf-8
"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""

import multiprocessing
def even_numbers():
    even = 0
    for i in range(1, 1000001):
        if i % 2 == 0:
            even += i
    print(even)


def not_even_numbers():
    not_even = 0
    for n in range(1, 1000001):
        if n % 2 != 0:
            not_even += n
    print(not_even)

if __name__  == '__main__':
    p1 = multiprocessing.Process(target=even_numbers())
    p2 = multiprocessing.Process(target=not_even_numbers())

    p1.start()
    p2.start()