class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: ₹{self.price}")


class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        # Initialize parent class
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        # Display product details first
        self.display_product()
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty} years")


class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        # Initialize parent class
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        # Display electronic product details first
        self.display_electronic_product()
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")

mobile = MobilePhone("Galaxy S25", 79999, "Samsung", 2, 12, 256)
mobile.display_mobile_details()
