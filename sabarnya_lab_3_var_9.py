import shelve
from sabarnya_lab_3_var_7 import Person, Manager  # Обов'язково для десеріалізації об'єктів

# Відкриваємо файл бази даних
db = shelve.open('persondb')

print("--- Поточні дані в БД перед оновленням ---")
for key in sorted(db):
    # Виведення в форматі: Ім'я => [Дані об'єкта]
    print(key, '\t=>', db[key])

# 1. Витягуємо об'єкт за ключем
if 'Sue Jones' in db:
    sue = db['Sue Jones']

    # 2. Змінюємо об'єкт у пам'яті (викликаємо метод класу Person)
    sue.giveRaise(0.10)

    # 3. Записуємо змінений об'єкт назад у сховище
    db['Sue Jones'] = sue
    print("\nЗарплату Sue Jones оновлено!")
else:
    print("\nПомилка: Sue Jones не знайдено в базі даних.")

# Закриваємо файл, щоб зберегти зміни на диску
db.close()