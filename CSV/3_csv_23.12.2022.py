#encoding:utf-8
"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""
import csv

data = [
    ['name', 'teacher', 'like_points'],
    ['Базы данных', "Голоднюк", 1],
    ['Программирование', 'Бабченок', 8],
    ['Сети', 'Головин', 4],
    ['Кмбербезопаасность', 'Кулаков', 8]
]

with open('Korelin.csv', 'w') as f:
    writer = csv.writer(f)
    for i in data:
        writer.writerow(i)
