# # Longest substring length without repeating the characters.,
#
# # my_string = "abcabcbb"
#
# def long_substring(s):
#     char_set = set()
#     l = 0
#     result = 0
#
#     # for r in range(len(s)):
#     #     while s[r] in char_set:
#     #         char_set.remove(s[l])
#     #         l += 1
#     #     char_set.add(s[r])
#     #     result = max(result, r-l+1)
#     # return result, "".join(char_set)
#
#     for r in range(len(s)):
#         while s[r] in char_set:
#             char_set.remove(s[l])
#             l += 1
#         char_set.add(s[r])
#         result = max(result, r-l+1)
#     return result
#
#
# print(long_substring('abcdabc'))
#
#
# print(long_substring('abcabbcabdcbb'))

def longest_prefix(l: list):
    min_str = min(l)
    max_str = max(l)
    for i, c in enumerate(min_str):
        if c != max_str[i]:
            return min_str[0: i]
    return min_str

    pass


ls = ["forwwarzd", "forevezr", "forwszt"]
print(longest_prefix(ls))




