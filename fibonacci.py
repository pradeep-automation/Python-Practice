def fibonacci(num):

    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0,1]
    else:
        fib_series = [0,1]
        while len(fib_series) < num:
            next_term = fib_series[-1] + fib_series[-2]
            fib_series.append(next_term)
        return fib_series

print(fibonacci(8))

# def add_numbers():
#     n = 0
#     i = 0
#     while i < len(range(11)):
#         n += i
#         i += 1
#     return n
#
# print(add_numbers())



