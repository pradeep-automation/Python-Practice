# def lengthOfLastWord(s: str) -> int:
#     st = s.rstrip()
#     stt = reversed(st)
#     return len(stt[1])


s = "Hello World   "
# print(lengthOfLastWord(s))

st = s.rstrip()
stt = "".join(reversed(s.rstrip())).split()
print(len(stt[0]))

