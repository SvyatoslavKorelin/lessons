"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""


from random import randint
from time import sleep
dice1 = randint(1, 6)
dice2 = randint(1, 6)
sleep(2)
print(dice1, dice2)

