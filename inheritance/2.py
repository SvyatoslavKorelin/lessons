# encoding=utf-8
class Rectangle():
    def __init__(self, dlina, shirina):
        self.dlina = dlina
        self.shirina = shirina
    def info(self):
        print('Дан прямоугольник с длинной', self.dlina, 'и шириной', self.shirina)

    def perimeter(self):
        return 2*self.dlina + 2*self.shirina

    def square(self):
        return self.dlina * self.shirina

rect = Rectangle(4, 2)
rect.info()
print(rect.perimeter())
print(rect.square())

