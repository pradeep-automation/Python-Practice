# def sq_nums(ls: list):
#     result = []
#     for num in ls:
#         yield num**2
#
#
# l = [1, 3, 5, 7]
# my_nums = sq_nums(l)
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # try:
# #     print(next(my_nums))
# # except StopIteration:
# #     print("Hiiiii")
#
# print(list(my_nums))
# for num in my_nums:
#     print(num)
#
#
# x = [2, 4, 8]
#
# m = map(lambda n: n**2, x)
# print(next(m))
# print(next(m))
# print(next(m))

# def two_sums(nums: list, target: int):
#     complements = {}
#     for index, num in enumerate(nums):
#         comp = target - num
#         if comp in complements:
#             return [complements[comp], index]
#         complements[num] = index
#     return -1
#
#
# l = [1, 4, 15, 7, 10, 9]
# tar = 11
# print(two_sums(l, tar))

# dic = {"fn": "pradeep", "age": 34}
# dic["ln"] = "ramola"
# print(dic)


# Input: s = "abcabcabcabc" #if aba---> False
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


