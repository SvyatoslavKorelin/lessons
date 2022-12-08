# encoding=utf-8
class Man():
    def quak(self):
        print('Имитирует кряканье')

    def wearclothes(self):
        print('Человек в пальто')


class Duck():
    def quak(self):
        print('Крякает')

    def wearclothes(self):
        print('Утка в шапке')


person = Man()
animal = Duck()

for s in (person, animal):
    s.quak()
    s.wearclothes()