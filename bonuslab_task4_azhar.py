class Car:
    def _init_(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def display_car(self):
        print(f"{self.year} {self.make} {self.model}, Color: {self.color}, Mileage: {self.mileage} ")

# Создаем несколько экземпляров класса Car
auto_first = Car("Toyota", "Camry", 2022, "Blue", 15000)
auto_second= Car("Honda", "Civic", 2020, "Red", 20000)
auto_third = Car("Ford", "Escape", 2021, "Silver", 18000)

# Выводим информацию о каждой машине с использованием метода display_car()
auto_first.display_car()
auto_second.display_car()
auto_third.display_car()