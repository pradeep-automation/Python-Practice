def longest_common_sub(strs):
    if not strs:
        return ""
    min_str = min(strs)
    # print(min_str)
    max_str = max(strs)
    # print(max_str)
    for i, char in enumerate(min_str):
        if char != max_str[i]:
            return min_str[:i]

    return min_str


ls = ["flower", "flow", "flight"]

print(longest_common_sub(ls))




