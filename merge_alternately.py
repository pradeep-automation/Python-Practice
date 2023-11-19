# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.
#
# Return the merged string.

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

def merge_alternately(word1: str, word2: str):

    result = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1
    return "".join(result)
    # l1 = [word for word in word1]
    # l2 = [word for word in word2]
    # res = ""
    # if len(l1) == len(l2):
    #     for i in range(len(word1)):
    #         res = res + l1[i] + l2[i]
    # elif len(l1) > len(l2):
    #     for i in range(len(word1)):
    #         if i < len(l2):
    #             res = res + l1[i] + l2[i]
    #         else:
    #             res = res + l1[i]
    # elif len(l1) < len(l2):
    #     for i in range(len(word2)):
    #         if i < len(l1):
    #             res = res + l1[i] + l2[i]
    #         else:
    #             res = res + l2[i]

    # return res


word1 = "abc"
word2 = "pqrde"
print(merge_alternately(word1, word2))
