expr = "abcbj"

def longsubstring(st):

    my_set = set()
    l = 0
    result = 0
    for r in range(len(st)):
        while st[r] in my_set:
            my_set.remove(st[l])
            l += 1
        my_set.add(st[r])
        result = max(result, r-l+1)
    return result


print(longsubstring(expr))
#
# expr = "abcabcabcabc"
# subx = "abc"
#
# def is_substring_multiple(st):
#     n = len(st)
#     # m = len(sub)
#     for i in range(1, len(st)//2 + 1):
#         if n % i == 0 and st[:i] * (n//i) == st:
#             return True
#     return False
#
#
# print(is_substring_multiple(expr))


exp= "My Cat is Jumping on the floor"

#
# def longest(expr: str):
#     ls = expr.split()
#     longest_char = ""
#     for item in ls:
#         if len(item) > len(longest_char):
#             longest_char = item
#     return longest_char
#
#
# print(longest(exp))





