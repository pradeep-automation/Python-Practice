def is_perfect_bracket(expr):
    my_dict = {
        '{': '}',
        '[': ']',
        '(': ')'
            }
    stack = []
    if expr and expr[0] in my_dict.values():
        return False

    for c in expr:
        if c in my_dict.keys():
            stack.append(c)
        elif c in my_dict.values():
            if not stack or my_dict[stack[-1]] != c:
                return False
            stack.pop()
    return len(stack) == 0



    # stack = []
    # for char in expr:
    #     if char in ['(', '[', '{']:
    #         stack.append(char)
    #     elif char == ')':
    #         if not stack or stack[-1] != '(':
    #             return False
    #         elif stack:
    #             stack.pop()
    #     elif char == '}':
    #         if not stack or stack[-1] != '{':
    #             return False
    #         elif stack:
    #             stack.pop()
    #     elif char == ']':
    #         if not stack or stack[-1] != '[':
    #             return False
    #         elif stack:
    #             stack.pop()
    # if stack:
    #     return False
    #
    # return True




# print(is_perfect_bracket('((())'))
#
# def is_perfect(expr):
#     open_brac = 0
#
#     for c in expr:
#         if c == '(':
#             open_brac += 1
#         if c == ')':
#             open_brac -= 1
#             if open_brac < 0:
#                 return False
#     return open_brac == 0


print(is_perfect_bracket('[]'))

