class InventorySystem:
    def _init_(self):
        self.inventory = []

    def add_item(self, name, quantity, description):
        item = {"Name": name, "Quantity": quantity, "Description": description}
        self.inventory.append(item)
        print(f"{name} added to inventory.")

    def display_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"Name: {item['Name']}, Quantity: {item['Quantity']}, Description: {item['Description']}")

    def change_quantity(self, name, new_quantity):
        for item in self.inventory:
            if item["Name"] == name:
                item["Quantity"] = new_quantity
                print(f"Quantity of {name} updated to {new_quantity}.")
                return
        print(f"Item '{name}' not found in inventory.")

# Создаем экземпляр системы отслеживания запасов
inventory_s = InventorySystem()

# Добавляем предметы в инвентарь
inventory_s.add_item("Laptop", 10, "High-performance laptops.")
inventory_s.add_item("Printer", 5, "Color laser printers.")
inventory_s.add_item("Mouse", 20, "Wireless optical mice.")

# Отображаем инвентарь
inventory_s.display_inventory()

# Изменяем количество предмета
inventory_s.change_quantity("Laptop", 8)

# Отображаем обновленный инвентарь
inventory_s.display_inventory()