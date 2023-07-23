def highest_sum(nums:list):
    highest = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            sum = nums[i] + nums[j]
            if sum >= highest and i != j:
                highest = sum
    return highest

ls = [2, 7, 11, 6, 17, 23, 45]
print(highest_sum(ls))
