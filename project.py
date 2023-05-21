class Product:
    def __init__(self, name, type, place, warranty):
        self.name = name
        self.type = type
        self.place = place
        self.warranty = warranty

    def __str__(self):
        return f"Product{{name='{self.name}', type='{self.type}', place='{self.place}', warranty={self.warranty}}}"


class ProductService:
    def __init__(self):
        self.products = []

    def addProduct(self, p):
        self.products.append(p)

    def getAllProducts(self):
        return self.products

    def getProduct(self, name):
        for p in self.products:
            if p.name == name:
                return p
        return None

    def getProductsByPlace(self, place):
        str_ = place.lower()
        prods = [p for p in self.products if str_ in p.place.lower()]
        return prods

    def getProductsByExpiredWarranty(self, year):
        prods = [p for p in self.products if p.warranty < year]
        return prods

    def getProductWithText(self, text):
        str_ = text.lower()
        prods = [p for p in self.products if str_ in p.name.lower() or str_ in p.type.lower() or str_ in p.place.lower()]
        return prods


if __name__ == '__main__':
    service = ProductService()

    # Add products to the service
    service.addProduct(Product("Type C", "Cable", "Black Drawer", 2024))
    service.addProduct(Product("Mac Studio", "Computer", "White Table", 2025))
    service.addProduct(Product("Focusrite Mixer", "Audio System", "White Table", 2025))
    service.addProduct(Product("Asus Vivobook", "Laptop", "Brown Drawer", 2021))
    service.addProduct(Product("Asus Rog", "Laptop", "Black Table", 2021))
    service.addProduct(Product("Macbook pro", "Laptop", "Brown Drawer", 2022))
    service.addProduct(Product("Wacom Pad", "Writing Pad", "Black Drawer", 2020))
    service.addProduct(Product("Apple Keyboard", "Keyboard", "White Table", 2022))
    service.addProduct(Product("Logitech Keyboard", "Keyboard", "Black Table", 2024))
    service.addProduct(Product("Hdmi cable", "Cable", "Black Drawer", 2024))
    service.addProduct(Product("Java Black Book", "Cable", "Shelf", 2024))
    service.addProduct(Product("Logi Mouse", "Mouse", "Black Table", 2022))
    service.addProduct(Product("Apple Mouse", "Mouse", "White Table", 2022))
    service.addProduct(Product("Lenovo Mouse", "Mouse", "Black Drawer", 2022))
    service.addProduct(Product("BlackBeast", "Computer", "White Table", 2020))

    products = service.getAllProducts()
    for p in products:
        print(p)
    print("==============================================")

    print("Search by place: Black Drawer")
    prods = service.getProductsByPlace("Black Drawer")
    for p in prods:
        print(p)
    print("==============================================")

    print("Search by expired warranty: 2023")
    prods = service.getProductsByExpiredWarranty(2023)
    for p in prods:
        print(p)
    print("==============================================")

    print("Search by text: black")
    prods = service.getProductWithText("black")
    for p in prods:
        print(p)
