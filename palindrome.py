def is_palindrome_recursion(s):
  if len(s)<=1:
      return True
  if s[0] == s[-1]:
      return is_palindrome_recursion(s[1:-1])
  else:
      return False

s = "racer"
print(is_palindrome_recursion(s))
print(is_palindrome_recursion("radar"))

print(is_palindrome_recursion("racecar"))
# print(s[0])
# print(s[-1])


# def is_palindrome(s):
#     left, right = 0, len(s)-1
#
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
#
# print(is_palindrome("xyzxyx"))



