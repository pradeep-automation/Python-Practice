# class Parent:
#
#     def show(self):
#         print("I am parent show")
#
#
# class Child(Parent):
#     pass
#
#     def show(self):
#         print("I am child show")
#
# class Sibling(Parent):
#     pass
#
#     def show(self):
#         print("I am sibling show")
#
#     def dislay(self):
#         print("I am sibling display")
#
# class GrandChild(Child, Sibling):
#     pass
#
#
# gc = GrandChild()
# gc.show()
# print(GrandChild.mro())
# gc.dislay()


# def add(*args):
#     total = 0
#     for i in args:
#         total = total + i
#     return total
#
#
# print(add(1, 4))
# print(add(1, 4, 7, 3))
# print(add(1, 4, 1, 34, 10))

def deco_func(original_func):
    def wrapper(*args):
        res = original_func(*args)

        return res
    return wrapper

@deco_func
def real_func(a, b):
    print("Hello World" + str(a+b))



# print(type(real_func))
real_func(3, 5)
