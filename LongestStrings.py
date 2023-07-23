# Longest substring length without repeating the characters.

# my_string = "abcabcbb"

def long_substring(s):
    char_set = set()
    l = 0
    result = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        result = max(result, r-l+1)
    return result


print(long_substring('abcabcbbcdags'))


# def long_substring(my_string):
#     if not my_string:
#         return 0
#
#     seen = {}   # Dictionary to store the last seen index of each character
#     start = 0   # start index of the current window
#     max_length = 0  # Length of the longest substring found so far
#
#     for i, char in enumerate(my_string):
#         if char in seen and seen[char] >= start:
#             # If the character is already seen in the current window,
#             # update the start index to the next position of the repeated character.
#             start = seen[char] + 1
#
#             # Update the last seen index of the character.
#         seen[char] = i
#
#         # Calculate the length of the current window.
#         current_length = i - start + 1
#
#         # Update the maximum length if needed.
#         max_length = max(max_length, current_length)
#
#     return max_length
#
#
#
#
# print(long_substring("abcabcbb"))


def substr(s):
    my_Set = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in my_Set:
            my_Set.remove(s[l])
            l +=1
        my_Set.add(s[r])
        res = max(res, r-l+1)
    return res



print(substr('pycpycddpcyp'))




