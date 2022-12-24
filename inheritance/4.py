# encoding=utf-8
class Bus():
    def __init__ (self, speed, capacity, max_speed, empty_seats):
        self.speed = speed
        self.capacity = capacity
        self.max_s = max_speed
        self.empty = empty_seats

    def Load(self, passengers):
        if self.empty > 0:
            self.empty -= passengers
            print('Посадили -', passengers)
        else:
            count = self.empty
            print('Посадили', self.empty)
            self.empty = 0

    def GainSpeed(self, speed):
        if speed + self.speed < self.max_s:
            self.speed += speed
            print('Разогналичь до - ', self.speed + speed)
        else:
            print('Достигнута максимальная скорость - ', self.max_s)
            self.speed == self.max_s

Ikarus = Bus(40, 40, 150, 36)
Ikarus.Posadka(5)
Ikarus.GainSpeed(50)





