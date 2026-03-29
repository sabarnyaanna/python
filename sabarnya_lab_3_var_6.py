# Файл person.py - опис класів

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = float(pay)

    def lastName(self):
        # Метод, який повертає останнє слово з імені (прізвище)
        return self.name.split()[-1]

    def giveRaise(self, percent):
        # Метод для зміни оплати
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        # Рядок для зручного виведення об'єкта
        return '[%s, %s, %s]' % (self.name, self.job, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        # Виклик конструктора суперкласу зі значенням job='mgr'
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=0.10):
        # Виклик методу суперкласу з додаванням бонусу
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':  # Блок для тестування
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)
    print(sue)
    print(bob.lastName(), ';', sue.lastName())

    sue.giveRaise(0.10)  # Збільшення зарплати для Person
    print(sue)

    print("-" * 20)

    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.10)  # Виклик адаптованої версії для Manager
    print(tom.lastName())  # Виклик успадкованого методу
    print(tom)  # Виклик успадкованого __str__