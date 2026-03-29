from sabarnya_lab_3_var_7 import Person, Manager
import shelve

# 1. Створення об'єктів (виправлено лапки)
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

# 2. Відкриття сховища
# shelve автоматично створить файл (наприклад, persondb.bak, .dat, .dir)
db = shelve.open('persondb')

# 3. Збереження об'єктів
# Змінено 'object' на 'obj', щоб не конфліктувати з системним типом object
for obj in (bob, sue, tom):
    db[obj.name] = obj # Використовуємо ім'я як ключ

# 4. Закриття сховища
db.close()
print("Дані успішно збережені у shelve!")