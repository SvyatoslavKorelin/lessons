# encoding=utf-8
from datetime import date



class AgesOfPeople:
    def init(self, name):
        self.name = name

    def printinfo(self):
        return (self.name)


    @classmethod
    def classmethod(cls, year_birth):
        age = (date.today().year - year_birth)
        return age

    @staticmethod
    def staticmethod(year_birth):
        age = (date.today().year - year_birth)
        if age < 18:
            return 'Несовершеннолетний'
        else:
            return 'Совершеннолетний'