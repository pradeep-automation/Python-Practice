def highest_sum(nums:list):
    # highest = 0
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         sum = nums[i] + nums[j]
    #         if sum >= highest and i != j:
    #             highest = sum
    # return highest
    high = 0
    sec_high = 0
    for num in nums:
        if num > high:
            sec_high = high
            high = num
        elif num > sec_high:
            sec_high = num
    return high + sec_high

ls = [2, 7, 11, 6, 17, 23, 45]
print(highest_sum(ls))
