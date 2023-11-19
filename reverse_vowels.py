# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and
# they can appear in both lower and upper cases, more than once.

# Example 2:
#
# Input: s = "leetcode"
# Output: "leotcede"

def reverseVowels(s: str):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    lst = [c if c not in vowels else '_' for c in s]
    lst_vowels = [c for c in s if c in vowels]

    for i in range(len(lst)):
        if lst[i] == '_':
            lst[i] = lst_vowels.pop()
    return "".join(lst)


print(reverseVowels("A man, a plan, a canal -- Panama"))

