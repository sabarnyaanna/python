class MyClass:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == 'secret_field':
            if object.__getattribute__(self, 'password') == '9ea)fc':
                return 'secret value'
            else:
                raise AttributeError("Неправильний пароль або доступ заборонено")
        else:
            return object.__getattribute__(self, item)


obj = MyClass()

# Спроба отримати secret_field без пароля
# print(obj.secret_field)  # AttributeError

# Встановлюємо правильний пароль
obj.password = '9ea)fc'
print(obj.secret_field)  # 'secret value'