"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example: Input: nums = [2,7,11,15], target = 9

"""


def two_sums(nums, target):
    complements = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return [complements[complement], index]
        complements[num] = index
    return


nums = [7, 11, 15, 2]
target = 9

print(two_sums(nums, target))





