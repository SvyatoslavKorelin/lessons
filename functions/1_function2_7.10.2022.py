"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""
def num(a, b, c):
    if a and b and c:
        print(a, b, c)


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    num(a, b, c)


main()