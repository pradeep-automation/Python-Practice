from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("woof")


class Cat(Animal):
    def speak(self):
        print("meow")


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            raise ValueError("Not a valid animal type")


factory = AnimalFactory()
dog = factory.create_animal("Dog")
try:
    cat = factory.create_animal("Cat")
except ValueError as v:
    print(v)
else:
    cat.speak()

dog.speak()
# cat.speak()



class Drugs(ABC):
    @abstractmethod
    def usage(self):
        pass

class RX(Drugs):
    def usage(self):
        print("I am rx ")



class Food(Drugs):
    def usage(self):
        print("I am food")


class DrugsFactory:
    def create_product(self, name):
        if name == "RX":
            return RX()
        elif name == "food":
            return Food()
        else:
            return "Incorrect type"

fac = DrugsFactory()
rx = fac.create_product("RX")
food = fac.create_product("food")
you = fac.create_product("You")
print(you)
rx.usage()
food.usage()
# you.usage()





