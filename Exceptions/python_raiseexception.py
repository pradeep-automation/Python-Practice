class CoffeeCup:
    def __init__(self, temp):
        self.temp = temp

    def drink_coffee(self):
        if self.temp > 75:
            raise ValueError("Coffee is too hot")
        elif self.temp < 65:
            raise ValueError("Coffee is too cold")
        else:
            print("good to drink")


mycup = CoffeeCup(64)
try:
    mycup.drink_coffee()
except ValueError as e:
    print(e)
