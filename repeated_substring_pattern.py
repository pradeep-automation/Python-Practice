# Input: s = "abcabcabcabc" #if aba---> False
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

def repeatedSubstringPattern(s: str) -> bool:
    n = len(s)
    for i in range(1, n//2+1):
        if n%i == 0 and s[:i] * (n//i) == s:
            return True
    return False


print(repeatedSubstringPattern("ababa"))

# from abc import ABC, abstractmethod

