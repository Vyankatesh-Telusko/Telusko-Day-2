# Telusko-Day-2
Project: Product Management App

## Assignment Tasks:

### Implement search by place:
##### def getProductsByPlace(self, place):
#####     str_ = place.lower()
#####     prods = []
#####     for p in self.products:
#####         place = p.place.lower()
#####         if str_ in place:
#####             prods.append(p)
#####     return prods
    
The getProductsByPlace method takes a place parameter and returns a list of products that have a matching place.

### Implement search by expired warranty:
##### def getProductsByExpiredWarranty(self, year):
#####     prods = []
#####     for p in self.products:
#####         if p.warranty < year:
#####             prods.append(p)
#####     return prods
    
The getProductsByExpiredWarranty method takes a year parameter and returns a list of products whose warranty has expired before the given year.

### Implement Stream API using list comprehensions:
##### def getProductWithText(self, text):
#####     str_ = text.lower()
#####     prods = [p for p in self.products if str_ in p.name.lower() or str_ in p.type.lower() or str_ in p.place.lower()]
#####     return prods
    
The getProductWithText method uses a list comprehension to create a list of products that match the given text in either name, type, or place.



![image](https://github.com/Vyankatesh-Telusko/Telusko-Day-2/assets/134121798/8f5bda85-a379-4555-bab6-7e8078a1d6d8)

![image](https://github.com/Vyankatesh-Telusko/Telusko-Day-2/assets/134121798/fbda1154-0503-4e92-9077-98d5204b0a4c)
