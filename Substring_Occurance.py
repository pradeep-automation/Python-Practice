# Find all occurrences of a substring in a given string.
# expr = "ababcabcbc", sub = "abc"

def find_occurrences(expr, sub):
    n = len(expr)
    m = len(sub)
    indices = []

    for index in range(n-m+1):
        if expr[index:index+m] == sub:
            indices.append(index)
    return indices


print(find_occurrences("pabcdabcdabc", "abc"))

st = "pradeepprincepratap"
print(st.find("pr"))  # return -1 if sub not found
print(st.index("pr"))    # raise ValueError if sub not found










