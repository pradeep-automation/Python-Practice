def lengthOfLastWord(s: str):
    # # st = s.rstrip()
    # stt = "".join(reversed(s.rstrip())).split()
    # print(len(stt[0]))
    last_word_len = 0
    # word_started = False
    for char in s:
        if char != " ":
            last_word_len += 1
            # word_started = True
        else:
            last_word_len = 0
            # word_started = False
    return last_word_len




sr = "Hello World Pradeep   "
print(lengthOfLastWord(sr.rstrip()))

