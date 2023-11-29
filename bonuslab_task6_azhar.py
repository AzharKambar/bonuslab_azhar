class ElectricCar(Car):
    def _init_(self, make, model, year, color, mileage, battery_size):
        super()._init_(make, model, year, color, mileage)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Размер батареи: {self.battery_size}")

# Создаем экземпляр ElectricCar
electriccar_auth= ElectricCar("Zeekr", "Model EV", 2023, "Orange", 6000, 200)

# Используем методы из класса Car
electriccar_auth.display_car()

# Используем методы из класса ElectricCar
electriccar_auth.describe_battery()