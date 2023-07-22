def count_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"
    count_vowels = 0
    for c in input_string:
        if c in vowels:
            count_vowels += 1
    count_cons = len(input_string) - count_vowels
    return f"# of vowels ---->{count_vowels} and #of consonants ----> {count_cons} in the String"


print(count_vowels_consonants((input("My string is= "))))
