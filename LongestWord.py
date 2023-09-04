# Write a Python function that takes a sentence as input and
# returns the longest word in the sentence.
# If multiple words have the same maximum length, return the first occurrence.


# def longest_word(s):
#     ls = s.split(" ")
#     return max(ls, key=len)
#
#
# sentence = "The quick brown fox jumped over the lazy dog"
# print(longest_word(sentence))


def longest_word(sentence):
    words = sentence.split(" ")
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


sen = "The quick brown fox jumped over the lazy diiiiiog"

print(longest_word(sen))
