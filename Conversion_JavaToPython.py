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
        self.products = []  # Initialize an empty list to store products

    def addProduct(self, p):
        self.products.append(p)  # Add a product to the list

    def getAllProducts(self):
        return self.products  # Return all the products

    def getProduct(self, name):
        for p in self.products:  # Iterate over the products
            if p.name == name:  # Check if the name matches
                return p  # Return the product if found
        return None  # Return None if no matching product is found

    def getProductWithText(self, text):
        str_ = text.lower()
        prods = []
        for p in self.products:  # Iterate over the products
            name = p.name.lower()
            type_ = p.type.lower()
            place = p.place.lower()
            if str_ in name or str_ in type_ or str_ in place:  # Check if the text is present in name, type, or place
                prods.append(p)  # Add the product to the result list
        return prods  # Return the list of products


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
    for p in products:  # Iterate over all the products
        print(p)  # Print each product
    print("==============================================")

    print("a Particular product")
    product = service.getProduct("Logi Mouse")  # Get a specific product by name
    print(product)  # Print the product

    print("==============================================")
    print("a Particular text")

    prods = service.getProductWithText("black")  # Get products with matching text
    for product in prods:  # Iterate over the products
        print(product)  # Print each product
