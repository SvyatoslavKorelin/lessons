# encoding=utf-8
class BankAccount():
    def __init__(self, name, balance, password):
        self._name = name
        self.__balance = balance
        self.__password = password
    def change_passport(self):
        oldpassword = int(input('введите пароль'))
        newname = input('введите новое имя')
        if oldpassword == self.__password:
            newname == self._name
            print('Имя заменено на '+ newname)
        elif oldpassword != self.__password:
            print('Неправильный пароль')

    def writedown_ballance(self):
        changing = int(input("введите сумму списания"))
        if changing > self.__balance:
            print('Невозможно')
        else:
            self.__balance = self.__balance + changing
            print('успешно ' + str(self.__balance))

    def writeup_ballance(self):
        changing = int(input('введите сумму зачисления'))
        a = self.__balance
        self.__balance = a + changing
        print('успешно ' + str(self.__balance))


account1 = BankAccount('Oleg', 3500, 892)
account1.change_passport()
account1.writeup_ballance()
account1.writedown_ballance()


