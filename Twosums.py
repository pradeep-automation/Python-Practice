"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example: Input: nums = [2,7,11,15], target = 9

"""
nums = [2, 11, 7, 15]
target = 18

def two_sums(nums, target):
    complements = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return [index, complements[complement]]
        complements.update({num: index})
    return


print(two_sums(nums, target))
















#
# def two_sum(nums, target):
#     complements = {}
#
#     for index, num in enumerate(nums):
#         complement = target - num
#         if complement in complements:
#             return [complements[complement], index]
#         complements[num] = index
#     return []
#
#
# ls = [2,5,15,10,35,20]
# print(two_sum(ls, 25))


