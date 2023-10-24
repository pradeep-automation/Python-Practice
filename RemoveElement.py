# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5,
# with the first five elements of nums containing 0, 0, 1, 3, and 4.

# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).


def remove_element(nums:list, val:int):
    index = 0
    count = nums.count(2)
    print(count)
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    c = 0
    while c < count:
        nums.pop()
        c += 1
    z = 0
    while z < count:
        nums.append("-")
        z += 1



    return nums

nums = [0,1,2,2,3,0,4,2]
val=2

print(remove_element(nums, val))


import datetime
import pytz
# 20230727021844278_R

current_timestamp = datetime.datetime.now()
print(current_timestamp.astimezone(pytz.timezone('America/Los_Angeles')))

