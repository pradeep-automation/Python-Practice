def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


fib_gen = fibonacci()

# Generate fib number one at a time
for _ in range(10):
    print(next(fib_gen))


def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

fib_g = fibo()
for n in range(5):
    print(next(fib_g))
