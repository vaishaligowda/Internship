# Parent Class
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)


# Child Class
class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")


# Grandchild Class
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# Creating object of MobilePhone
mobile = MobilePhone(
    "Smartphone",
    25000,
    "Samsung",
    2,
    "8 GB",
    "128 GB"
)

# Displaying all details
print("---- Mobile Phone Details ----")
mobile.display_product()
mobile.display_electronic_product()
mobile.display_mobile_details()