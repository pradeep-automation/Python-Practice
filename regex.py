import re

# pattern = r"apple"
#
# stmt = "apples are delicious, and apple pie is great."
#
# match = re.search(pattern, stmt)
# if match:
#     print("found")
# else:
#     print("not found")
# matches = re.findall(pattern, stmt)
# print(matches)
#
# my_stmt = "angle is new apple ample it"
# patt = r"a..le"
# print(re.findall(patt, my_stmt))


# pattern = r"\d+"
# pattern = r"[aeiou]"
# pattern = r"\d{2,4}"
# pattern = r"(apple|orange)"
pattern = r"^orange"
# pattern = r"orange$"
st = "orange are delicious, and Orange pie is great"
match = re.search(pattern, st, re.IGNORECASE)
print("hellllllo", match.group())

if match:
    print("yes")
else:
    print("No")

num_patt = r"92\d{3}90326122[27]\d{12}"
# num_pat = r"\d{29}"

track = "92748903261227000000000727"

matching = re.search(num_patt, track)

if matching:
    print("tracking yes")
else:
    print("tracking No")

# Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)

# Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub(r"(rain|Spain)", "9", txt)
print(x)
