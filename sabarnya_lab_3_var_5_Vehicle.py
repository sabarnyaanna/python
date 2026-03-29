class Vehicle:
    def __init__(self, brand, model, price=0):
        self.brand = brand
        self.model = model
        self.price = float(price)

    def getDescription(self):
        return f"{self.brand} {self.model}"

    def applyDiscount(self, percent):
        self.price = int(self.price * (1 - percent))

    def __str__(self):
        return f"[{self.__class__.__name__}: {self.brand} {self.model}, Ціна: {self.price}]"


class Truck(Vehicle):
    def __init__(self, brand, model, price, capacity):
        super().__init__(brand, model, price)
        self.capacity = capacity

    def applyDiscount(self, percent):
        actual_discount = percent - 0.05 if percent > 0.05 else 0
        super().applyDiscount(actual_discount)

    def loadCargo(self, weight):
        if weight <= self.capacity:
            return f"Успішно завантажено {weight}т на {self.brand}."
        return f"Помилка! {weight}т — це забагато для вантажності {self.capacity}т."

if __name__ == '__main__':
        my_car = Vehicle('Audi', 'A6', 50000)
        my_truck = Truck('BMW', 'X6', 120000, 20)
        print(my_car)
        print(my_truck)
        print(f"Опис: {my_car.getDescription()}")
        print(my_truck.loadCargo(15))
        my_truck.applyDiscount(0.10)
        print(f"Ціна вантажівки після знижки: {my_truck.price}")