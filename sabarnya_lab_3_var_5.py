# Файл person.py - опис класів

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = float(pay)

    def lastName(self):  # метод, який повертає прізвище
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # внесення змін

    def __str__(self):
        return '%s, %s, %s' % (self.name, self.job, self.pay)


class Manager(Person):
    def __init__(self, name, pay):  # перевизначений конструктор
        # Виклик конструктора суперкласу зі значенням job='mgr'
        super().__init__(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=0.10):
        # Виклик методу суперкласу з додатковим бонусом
        super().giveRaise(percent + bonus)


if __name__ == '__main__':  # файл запускають для тестування
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)
    print(sue)

    print(bob.lastName(), ';', sue.lastName())

    sue.giveRaise(0.10)  # використовують методи
    print(sue)

    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.10)  # Виклик адаптованої версії
    print(tom.lastName())  # Виклик успадкованого методу
    print(tom)             # Виклик успадкованого __str__