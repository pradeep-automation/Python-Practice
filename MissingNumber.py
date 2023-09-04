# Geekforgeeks1
def missingNumber(array, n):
    sum_num = n * (n + 1) / 2
    result = sum_num - sum(array)
    return int(result)




