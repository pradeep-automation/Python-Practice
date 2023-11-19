def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    reversed_num = 0
    temp = x
    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    return reversed_num == x


print(isPalindrome(1001))


def is_num_palin(x):
    temp = x
    rev = 0

    while temp != 0:
        digit = temp % 10
        rev = rev*10 + digit
        temp //= 10

    return rev==x







    # temp = x
    # reverse = 0
    # while temp != 0:
    #     digit = temp % 10
    #     reverse = reverse * 10 + digit
    #     temp //= 10
    # return reverse == x


print(is_num_palin(1011))











