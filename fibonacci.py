def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_s = [0, 1]
        while len(fib_s) < n:
            next_t = fib_s[-1] + fib_s[-2]
            fib_s.append(next_t)
        return fib_s


print(fibonacci(7))

# def add_numbers():
#     n = 0
#     i = 0
#     while i < len(range(11)):
#         n += i
#         i += 1
#     return n
#
# print(add_numbers())



