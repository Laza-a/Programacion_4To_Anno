class Device:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def display_details(self):
        print("Model:", self.model)
        print("Price:", self.price)


# Crear dos dispositivos
device1 = Device("iPhone 15", 800)
device2 = Device("Samsung Galaxy S24", 750)

# Mostrar información
device1.display_details()
print("")
device2.display_details()