# exp = "A man, a plan, a canal, Panama!"
#
# def is_palindrome(expr: str):
#     ls = []
#     # for char in expr:
#     #     if char.isalnum():
#     #         ls.append(char.lower())
#     # clean_str = "".join(ls)
#     clean_str = "".join(char.lower() for char in expr if char.isalnum())
#
#     l, r = 0, len(clean_str)-1
#
#     while l<r:
#         if clean_str[l] != clean_str[r]:
#             return False
#         l += 1
#         r -= 1
#     return True
#
# print(is_palindrome(exp))

def my_func():
    a, *b, c = ['car', 'dog', 'lion', 'cat']
    item = b

    return 'dog' in [item] or None

print(my_func())
