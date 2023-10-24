# def outer_func(x):
#
#     def inner_func(y):
#
#         return x+y
#     return inner_func
#
#
# closure = outer_func(10)
#
# print(closure(20))

def decorator_func(original_func):

    def wrapper_func():
        print("some before the actual method")
        original_func()
        print("some after the actual func")
    return wrapper_func

# @decorator_func
def real_func():
    print("Actual functionality")


deco = decorator_func(real_func)
deco()


# real_func()


