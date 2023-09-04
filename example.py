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


# prices = [2,5,6,1,3,8,7,13,11,20,25]
#
# def bestsell(prices):
#     max_p = 0
#     l = 0
#     r = 1
#     for r in range(len(prices)):
#         if prices[l] < prices[r]:
#             profit = prices[r] - prices[l]
#             max_p = max(max_p, profit)
#         else:
#             l = r
#     return max_p
#
#
# print(bestsell(prices))
"""
Example: Input: nums = [2,7,11,15], target = 9

"""
#
#
# def two_sums(nums, target):
#     complements = {}
#     for i, num in enumerate(nums):
#         comp = target - num
#
#         if comp in complements:
#             return [complements[comp], i]
#         complements[num] = i
#     return
#
#
# mynum = [2,7,11,15,18,12,6]
# tar = 18
# print(two_sums(mynum, tar))

def perfect_bracket(expr):
    stack = []
    for char in expr:
        if char in ['{','[','(']:
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            elif stack:
                stack.pop()
        elif char == '}':
            if not stack or stack[-1] != '{':
                return False
            elif stack:
                stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            elif stack:
                stack.pop()
    if stack:
        return False
    return True


# print(perfect_bracket('[(){}]'))

def is_perfect_bracket(expr):
    my_dict = {
        '{': '}',
        '[': ']',
        '(': ')'
            }
    stack = []

    for char in expr:
        if char in my_dict.keys():
            stack.append(char)
        elif char in my_dict.values():
            if not stack or my_dict[stack[-1]] != char:
                return False
            stack.pop()
    print(len(stack))
    return len(stack) == 0


print(is_perfect_bracket(']'))










