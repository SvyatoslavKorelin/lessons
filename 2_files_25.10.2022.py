"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open("test2.txt", "w+") as f:
   f.write('но у меня не получается')
   f.seek(0)
   text2 = f.read()
with open("test1.txt", "r") as b:
   text1 = b.read()
with open('test3.txt', 'w') as n:
   n.write(text1+", "+text2)


