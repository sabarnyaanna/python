import shelve
import dbm
from sabarnya_lab_3_var_5_Vehicle import Vehicle, Truck

if __name__ == '__main__':
    my_car = Vehicle('Audi', 'A6', 50000)
    my_truck = Truck('BMW', 'X6', 120000, 20)

    print("--- Тестування об'єктів ---")
    print(my_car)
    print(my_truck)
    print(my_truck.loadCargo(15))

    print("\n--- Збереження в Shelve ---")
    with shelve.open('vehicles_shelve') as db:
        db['Audi_Record'] = my_car
        db['BMW_Record'] = my_truck
    print("Об'єкти збережені!")

    with shelve.open('vehicles_shelve') as db:
        print("\nЗміст Shelve:")
        for key in db:
            print(f"Ключ: {key} => {db[key]}")

    print("\n--- Збереження в DBM (як рядки) ---")
    with dbm.open('vehicles_raw', 'c') as db:
        data = f"{my_car.brand}|{my_car.model}|{my_car.price}"
        db[b'car_1'] = data.encode('utf-8')
    print("Рядок збережено в DBM!")