# encoding=utf-8
class Main():
    def __init__(self, name):
        self.name = name

    def adding1(self):
        text = self.name + 'гений'

class NotMain(Main):
    def adding2(self, text, ):
        a = text + ',но его отчислят если он не будет изучать ОПП'

    def printing(self):
        print(a)

Slava = Main('Слава')
Slava.printing()