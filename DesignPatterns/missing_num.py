def missing_num(l: list):
    sum_l = sum(l)
    n = max(l)
    miss = (n * (n + 1)/2) - sum_l
    return miss


ls = [1, 4, 5, 2]
print(missing_num(ls))
