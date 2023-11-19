def reverse_num(num: int):
    rev = 0

    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    return rev


n = 125
print(reverse_num(n))

