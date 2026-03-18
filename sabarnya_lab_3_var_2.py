# Додано методи, які інкапсулюють операції

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    # метод «виведення прізвища»
    def lastName(self):
        return self.name.split()[-1]

    # метод «зміна зарплати»
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

    # використовуємо методи
    print(bob.lastName(), ';', sue.lastName())

    sue.giveRaise(0.10)
    print(sue.pay)