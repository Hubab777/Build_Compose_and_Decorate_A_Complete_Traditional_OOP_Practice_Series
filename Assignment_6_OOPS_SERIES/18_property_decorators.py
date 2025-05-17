class Product:
    def __init__(self, price):
        self.__price = price  # private attribute

    @property
    def price(self):
        print("Getting price...")
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            print("Setting price...")
            self.__price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self.__price

p = Product(200)

print(p.price)     # Getting price... → 200

p.price = 350      # Setting price...

print(p.price)     # Getting price... → 350

del p.price        # Deleting price...

