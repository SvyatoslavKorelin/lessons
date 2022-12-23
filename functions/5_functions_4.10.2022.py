"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.
Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""
def subjects_choose():
    stop = input('Для завершения программы введите "стоп"!').lower
    while stop != 'стоп':
        name = input('Введите ваше имя и число предметов.')
        num = int(input('Введите баллы по каждому предмету.'))
        summa = sum(num)
        print(summa)
        if summa > 80:
            print('Наградить дипломом.')
        elif summa > 50 and summa <= 80:
            print('Наградить похвальной грамотой')
        else:
            print('Выдать грамоту об учестии.')
    return


subjects_choose()