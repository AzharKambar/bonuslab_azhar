class Car:
    def _init_(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def display_car(self):
        print(f"{self.year} {self.make} {self.model}, Color: {self.color}, Mileage: {self.mileage}")

    def drive(self, distance):
        self.mileage += distance
        print(f"Drive {distance} miles. New mileage: {self.mileage} miles")

# Создаем экземпляр класса Car
car_auth= Car("Ferrari", "F40", 2023, "Red", 20000)

# Выводим информацию о машине
car_auth.display_car()

# Используем метод drive() для изменения пробега
car_auth.drive(100)

# Выводим обновленную информацию о машине
car_auth.display_car()