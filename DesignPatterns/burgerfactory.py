class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)


class BurgerFactory:

    def create_cheese_burger(self):
        ingredients = ["bun", "cheese", "Patty"]
        return Burger(ingredients)

    def create_beef_burger(self):
        ingredients = ["bun", "cheese", "Beef Patty", "Lettuce"]
        return Burger(ingredients)

    def create_vegan_burger(self):
        ingredients = ["bun", "special sauce", "veg Patty"]
        return Burger(ingredients)


burger_factory = BurgerFactory()
beef_burger = burger_factory.create_beef_burger()
burger_factory.create_cheese_burger().print()
burger_factory.create_vegan_burger().print()
print(beef_burger.ingredients)

var = str("5")

