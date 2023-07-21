st = 'Pradeep Ramola'

def reverse_string(s):
    rev_str = ""
    for c in s:
        rev_str = c + rev_str
    return rev_str

print(reverse_string(st))

