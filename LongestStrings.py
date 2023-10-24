# Longest substring length without repeating the characters.,

# my_string = "abcabcbb"

def long_substring(s):
    char_set = set()
    l = 0
    result = 0

    # for r in range(len(s)):
    #     while s[r] in char_set:
    #         char_set.remove(s[l])
    #         l += 1
    #     char_set.add(s[r])
    #     result = max(result, r-l+1)
    # return result, "".join(char_set)

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        result = max(result, r-l+1)
    return result


print(long_substring('abcdabc'))


print(long_substring('abcabbcabdcbb'))




