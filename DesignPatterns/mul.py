def longest_common(ls: list):
    common = ls[0]
    for item in ls:
        while common:
            count = 0
            if common not in item:
                count += 1
                common = common[:-count]
            else:
                break
    return common


l = ["forever", "forest", "foreigner", "Rocforegt"]

print(longest_common(l))
