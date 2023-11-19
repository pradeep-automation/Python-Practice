#Problem# 1431

def kidsWithCandies(candies: list[int], extraCandies: int):
    maxC = max(candies)
    result = [candy + extraCandies >= maxC for candy in candies]
    # for candy in candies:
    #     if candy + extraCandies >= maxC:
    #         result.append(True)
    #     else:
    #         result.append(False)
    return result


candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))

