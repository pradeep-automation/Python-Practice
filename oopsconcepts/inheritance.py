import time


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} and age is {self.age}"


class Dog(Pet):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    @staticmethod
    def speak():
        return "Woof"

    def __repr__(self):
        return f"{super().__repr__()} and breed is {self.breed}"

class Cat(Pet):

    def speak(self):
        return "Meow"


dog = Dog("Pradeep", 22, "Bhotia")
print(dog)

# Dog.speak()
# Cat.speak()
time.sleep(10)