# encoding=utf-8
class Hero:
    def unit_(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Поприветствовать героя', self.name)
        print('Уровень здоровья', self.health)
        print('Класс брони', self.armor)
        print('Уровень силы', self.power)
        print('Тип оружия', self.weapon)

    def strike(self, enemy):
        while self.health > 0 and enemy.health > 0:
        print(
            '-> УДАР' + self.name + 'атакует' + enemy.game +
            'с силой' + str(self.power) + 'б используя' + self.weapon +'\n')

        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
            print(
                enemy.name + 'покачнулся(-ась). \n Класс брони упал до '
                + str(enemy.armor) + ', а уровень здоровья до '
                + str(enemy.health) + '\n')
        elif enemy.armor > 0:
            print(str(enemy.name) + 'выдержал удар' + "\n осталось здоровья: " + str(enemy.health))
        elif enemy.health <= 0:
            print('Вы победели')

    def enemy_strike(self):
        print(
            '-> УДАР' + self.name + 'атакует' + self.name +
            'с силой' + str(self.power) + 'б используя' + self.weapon + '\n')

        self.armor -= self.power
        if self.armor < 0:
            self.health += self.armor
            self.armor = 0
            print(
                hero.name + 'покачнулся(-ась). \n Класс брони упал до '
                + str(self.armor) + ', а уровень здоровья до '
                + str(self.health) + '\n')
        elif self.armor > 0:
            print(str(self.name) + 'выдержал удар' + "\n осталось здоровья: " + str(self.health))
        elif self.health <= 0:
            print('Вы Погибли')

class Magician(Hero):
    def hello(self):
        print('Неспешной походкой вышел волбешник')
        self.print_info

    def strike(self, enemy):
        print(
            '-> УДАР' + self.name + 'атакует' + enemy.game +
            'с силой' + str(self.power) + 'б используя' + self.weapon + '\n')

        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
            print(
                enemy.name + 'покачнулся(-ась). \n Класс брони упал до '
                + str(enemy.armor) + ', а уровень здоровья до '
                + str(enemy.health) + '\n')
        elif enemy.armor > 0:
            print(str(enemy.name) + 'выдержал удар' + "\n осталось здоровья: " + str(enemy.health))
        elif enemy.health <= 0:
            print('Вы победели')

    def enemy_strike(self):
        print(
            '-> УДАР' + self.name + 'атакует' + self.name +
            'с силой' + str(self.power) + 'б используя' + self.weapon + '\n')

        self.armor -= self.power
        if self.armor < 0:
            self.health += self.armor
            self.armor = 0
            print(
                self.name + 'покачнулся(-ась). \n Класс брони упал до '
                + str(self.armor) + ', а уровень здоровья до '
                + str(self.health) + '\n')
        elif self.armor > 0:
            print(str(self.name) + 'выдержал удар' + "\n осталось здоровья: " + str(self.health))
        elif self.health <= 0:
            print('Вы Погибли')

