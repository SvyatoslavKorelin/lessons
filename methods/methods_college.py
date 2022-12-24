# encoding=utf-8
class A():
    def __init__ (self):
        self.number = 2

    def __radd__(self, other):
        return self.number + other.number
    def __lt__(self, other):
        return self.number < other.number
    def __gt__(self, other):
        return self.number > other.number


class B():
    def __init__(self):
        self.number = 3
        self.othernumber = 5
        self.anothernumber = 7

a = A()
b = B()
print(a < b)