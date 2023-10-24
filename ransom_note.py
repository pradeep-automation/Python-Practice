# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters
# from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
#
#
def can_construct(ransomNote, magazine):

    char_freq = {}
    for char in magazine:
        char_freq[char] = char_freq.get(char, 0) + 1

    for c in ransomNote:
        if char_freq.get(c, 0) == 0:
            return False
        char_freq[c] -= 1
    return True
#
print(can_construct("prdp", "pradeep"))
#
# print(can_construct("xyz", "xyzssedzysdse"))

from collections import Counter
def can_construct(ransomNote, magazine):
    st1 = Counter(ransomNote)
    st2 = Counter(magazine)
    if st1 & st2 == st1:
        return True
    return False


print(can_construct("aa", "axbbbb"))

print(can_construct("xyz", "xyzssedzysdse"))



