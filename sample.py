# def gen(n):
#     for i in range(n):
#         yield i**2
#
# genet = (i**3 for i in range(5))
#
# print(genet.__next__())
# print(genet.__next__())
# print(genet.__next__())
#
#
#
# next_term = gen(4)
# print(next_term.__next__())
# print(next_t;erm.__next__())
# print(next_term.__next__())
# # print(next_term.__next__())
#
# for val in next_term:
#     print(val)


# lam = lambda x: x**2
#
# print(lam(2))
#
# lam = list(filter(lambda x: x % 2 == 0, [1, 3, 4, 6, 11, 16]))
# lam2 = list(filter(lambda x: x != 0, (map(lambda x: x**3 if x % 2 == 0 else 0, [1, 3, 4, 6, 11, 16]))))
#
# print(lam)
# print(lam2)
#
# class Singleton:
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance
#
#     def __init__(self):
#         self.data = None
#
#     def set_data(self, data):
#         self.data = data
#
#     def get_data(self):
#         return self.data
#
#
# single1 = Singleton()
# single2 = Singleton()
# single1.set_data("pradeep")
#
# print(single2.get_data())
#
# st = "abcabcabcabc"
#
# def repeat(s):
#     n = len(s)
#
#     for i in range(1, n//2+1):
#         if n%i == 0 and s[:i] * (n//i) == s:
#             return True
#     return False
#
#
# print(repeat(st))


# longest substring without repeating the characters

ls = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 10]
# ls.sort(key=len)

# print(ls)
#
# def sort_list(lst: list):
#     n = len(lst)
#     for i in range(n):
#         for j in range(n-1):
#             # if lst[j] >= lst[j+1]:
#             #     lst[j], lst[j+1] = lst[j+1], lst[j]
#             if lst[i] >= lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#
#     return lst



# print(sort_list(ls))

#
# def sort_list(lst: list):
#     if len(lst) <= 1:
#         return lst
#     pivot = lst[len(lst)//2]
#     left = [x for x in lst if x < pivot]
#     middle = [x for x in lst if x == pivot]
#     right = [x for x in lst if x > pivot]
#     # r = list(filter(lambda x: x>pivot, lst))
#     # return right, "and", r
#
#     return sort_list(left) + middle + sort_list(right)
#
#
# print(sort_list(ls))


# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#
#     @abstractmethod
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
#
# class Cat(Animal):
#     def speak(self):
#         print("meow")
#
# class AnimalFactory:
#     def create_animal(self, animal):
#         if animal == "cat":
#             return Cat()
#         elif animal == "dog":
#             return Dog()
#
#
# fac = AnimalFactory()
# dog = fac.create_animal("dog")
# dog.speak()


# Find all occurrences of a substring in a given string.
exp = "ababcabcbc"
subs = "abc"

def find_occurrences(expr, sub):
    n = len(expr)
    m = len(sub)
    res = []
    for i in range(n-m+1):
        if expr[i:i+m] == sub:
            res.append(i)
    return res


print(find_occurrences(exp, subs))











