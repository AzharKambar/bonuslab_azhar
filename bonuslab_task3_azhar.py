class Car:
    def _init_(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_car(self):
        print(f"{self.year} {self.make} {self.model}")

# Создаем экземпляр класса Car
car_auth = Car("Ferrari", "F40", 2023)

# Выводим информацию о машине с помощью метода display_car()
car_auth.display_car()