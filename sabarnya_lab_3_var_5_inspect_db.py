import shelve

with shelve.open('vehicles_shelve') as db:
    print("--- Перевірка Shelve ---")
    for key in db:
        obj = db[key]
        print(f"Ключ: {key}")
        print(f"Дані об'єкта: {obj}")
        print(f"Тип: {type(obj)}")
        print("-" * 20)