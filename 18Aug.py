expr = "abcbj"

def longsubstring(st):

    my_set = set()
    l = 0
    result = 0
    for r in range(len(st)):
        while st[r] in my_set:
            my_set.remove(st[l])
            l += 1
        my_set.add(st[r])
        result = max(result, r-l+1)
    return result

#
# def long_sub(string):
#
#     ls = []
#     l = 0
#     result = 0
#
#     for r in range(len(string)):
#         while string[r] in ls:
#             ls.remove(string[l])
#             l += 1
#         ls.append(string[r])
#         result = max(result, r-l+1)
#     return result, "".join(ls)

st = "abcbjdfbbc"

# print(long_sub(st))
print(longsubstring(st))






