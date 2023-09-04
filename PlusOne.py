# def plusOne(digits: list[int]) -> list[int]:
#     res = []
#     for i in range(len(digits)):
#         if i == len(digits) - 1 and digits[i] != 9:
#             digits[i] = digits[i] + 1
#             res.append(digits[i])
#         else:
#             res.append(1)
#             res.append(0)
#         res.append(digits[i])
#
#
#     return res


digits = [9, 9, 9, 9]
string = ""
for n in digits:
    string += str(n)
temp = str(int(string) + 1)
res = []
for char in temp:
    res.append(int(char))

print(res)
