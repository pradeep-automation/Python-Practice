import math

#
# def divide_nums (a, b):
#     try:
#         result = a/b
#         # return result
#     except ValueError as v:
#         print(v)
#     except ZeroDivisionError:
#         print("Error: by zero is not allowed")
#     except TypeError as e:
#         print(f'error:{e}')
#
#     else:
#
#         print("when try passes", result)
#         return result
#
#
#     finally:
#         print("this will be always executed regardless of exceptions")
#
#
# try:
#     results = divide_nums(10, 4)
#     # results = divide_nums(10, "d")
#     # print(results)
#     print("Results: ",results)
# except ValueError as v:
#     print(v)


class MyException(Exception):

    def __init__(self, message="This is my exception"):
        self.msg = message
        super().__init__(self.msg)


def minus(a, b):
    if a - b != b:
        raise MyException
    return a-b

x = 10
y = 6
try:
    print(minus(x, y))
except MyException as e:
    print(e)







