# Input: numss = [1,2,3,4]
# Output: [24,12,8,6]

import math

def product_ex_self(nums: list):
    answer = []
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n

    left_product = 1
    for i in range(1, n):
        left_product *= nums[i-1]
        left_products[i] = left_product

    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i+1]
        right_products[i] = right_product

    result = [left_products[i] * right_products[i] for i in range(n)]

    return result




    # for i in range(len(nums)):
    #     num = nums.pop(i)
    #     item = math.prod(nums)
    #     answer.append(item)
    #     nums.insert(i, num)
    #
    # return answer



numss = [1,2,3,4]
print(product_ex_self(numss))
