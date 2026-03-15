class Car:
    def change_color(self, newcolor):
        self.color = newcolor

    def change_brand(self, newbrand):
        self.brand = newbrand

    def change_year(self, newyear):
        self.year = newyear

    def change_speed(self, newspeed):
        self.speed = newspeed

    def change_run(self, newrun):
        self.run = newrun

    def show_info(self):
        print(f"Марка: {self.brand}")
        print(f"Колір: {self.color}")
        print(f"Рік: {self.year}")
        print(f"Швидкість: {self.speed}")
        print(f"Пробіг: {self.run}")
    
cars = []
n = int(input("Введіть кількість авто, які ви хочете додати: "))

for i in range(n):
    print(f"\nАвто №{i+1}")
    car = Car()  
    car.brand = input("Введіть марку авто: ")
    car.color = input("Введіть колір: ")
    car.year = int(input("Введіть рік: "))
    car.speed = int(input("Введіть швидкість: "))
    car.run = int(input("Введіть пробіг: "))

    cars.append(car)

while True:
    print("\nСписок авто:")
    for idx, car in enumerate(cars):
        print(f"{idx+1}. {car.brand} ({car.year})")
    print("0. Вийти")

    choice = int(input("\nВиберіть авто для редагування (0 щоб вийти): "))
    if choice == 0:
        break

    if 1 <= choice <= len(cars):
        selected_car = cars[choice - 1]
        print("\nОбране авто:")
        selected_car.show_info()

        print("\nЩо хочете змінити?")
        print("1. Марка")
        print("2. Колір")
        print("3. Рік")
        print("4. Швидкість")
        print("5. Пробіг")
        print("0. Назад")

        change = int(input("Ваш вибір: "))
        if change == 1:
            new_brand = input("Введіть нову марку: ")
            selected_car.change_brand(new_brand)
        elif change == 2:
            new_color = input("Введіть новий колір: ")
            selected_car.change_color(new_color)
        elif change == 3:
            new_year = int(input("Введіть новий рік: "))
            selected_car.change_year(new_year)
        elif change == 4:
            new_speed = int(input("Введіть нову швидкість: "))
            selected_car.change_speed(new_speed)
        elif change == 5:
            new_run = int(input("Введіть новий пробіг: "))
            selected_car.change_run(new_run)
        elif change == 0:
            continue
        else:
            print("Невірний вибір!")

        print("\nОновлена інформація про авто:")
        selected_car.show_info()
    else:
        print("Невірний вибір авто!")