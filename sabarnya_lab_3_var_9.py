import dbm
from sabarnya_lab_3_var_6 import Person, Manager


def Transform(a):
    # Функція, яка перетворює рядок на список за роздільником ','
    # Прибираємо зайві пробіли та символи [ ] якщо вони є
    clean_string = a.replace('[', '').replace(']', '')
    return clean_string.split(", ")


# Відкриваємо сховище. Режим 'w' (write) або 'c' (create),
# бо 'n' завжди створює НОВУ порожню базу.
db = dbm.open('persondb_raw', 'c')

# Попередньо додамо дані (якщо база порожня), щоб код мав з чим працювати
if b'Sue Jones' not in db:
    db[b'Sue Jones'] = "Sue Jones, dev, 100000.0"

keys_list = list(db.keys())
print(f"Ключі в БД: {keys_list}")

# Відображення об'єктів у відсортованому порядку
for i in sorted(keys_list):
    print(i.decode(), '\t=>', db[i].decode())

print()

# Пошук та оновлення Sue Jones
k = len(keys_list)
sue_data = None

while k > 0:
    current_key = keys_list[k - 1]
    if current_key == b'Sue Jones':
        sue_data = db[current_key].decode()  # Витягуємо рядок
        print(f"Знайдено запис: {sue_data}")
        break
    k -= 1

if sue_data:
    # 1. Перетворюємо рядок у список
    parts = Transform(sue_data)  # ['Sue Jones', 'dev', '100000.0']

    # 2. Створюємо тимчасовий об'єкт Person для розрахунків
    # Важливо: pay має бути числом, тому використовуємо float()
    ssue = Person(parts[0], parts[1], float(parts[2]))

    # 3. Змінюємо дані методом класу
    ssue.giveRaise(0.10)

    # 4. Записуємо назад у dbm як рядок (метод __str__ спрацює автоматично)
    db[b'Sue Jones'] = str(ssue)
    print(f"Оновлений запис у БД: {db[b'Sue Jones'].decode()}")

db.close()