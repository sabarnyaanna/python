def outer_method(self):
    print('I am a method of object', self)

class MyClass:
    method = outer_method

obj = MyClass()
obj.method()


class MyClass:
    # Атрибут класу
    class_attribute = 8

    def __init__(self):
        self.data_attribute = 42

    # Статичний метод
    @staticmethod
    def static_method():
        print(MyClass.class_attribute)

    # Звичайний метод
    def instance_method(self):
        print(self.data_attribute)


if __name__ == '__main__':
    # Виклик статичного методу
    MyClass.static_method()

    # створення об'єкта
    obj = MyClass()

    # виклик методу
    obj.instance_method()

    # виклик статичного через об'єкт
    obj.static_method()