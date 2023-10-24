def is_prime(num):
    if num < 2:
        return False
    # for i in range(2, int(num**0.5)+1):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True


primes = [num for num in range(1, 100) if is_prime(num)]
print(primes)


def prime_nums(num1, num2):
    primes = []
    for num in range(num1, num2):
        if is_prime(num):
            primes.append(num)
    return primes


print(prime_nums(1, 100))
