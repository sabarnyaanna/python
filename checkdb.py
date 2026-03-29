import shelve
from sabarnya_lab_3_var_7 import Person, Manager # Обов'язково! Python має знати класи об'єктів

db = shelve.open('persondb')
print("--- Вміст бази даних ---")
for key in db:
    print(f"Ключ: {key}")
    print(f"Об'єкт: {db[key]}")
    print("-" * 10)
db.close()