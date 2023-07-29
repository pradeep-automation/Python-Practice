message = "Hello Python!"
# Indexing
print(message[7])
print(message[11])

# Slicing -- Starting index is inclusive and end index is exclusive

print(message[0:4])
print(message[4:8])

"""You can omit the start index in slicing to start from the beginning of the string, 
and omit the end index to slice until the end of the string:
"""
print(message[:5])
print(message[2:])
print(message[:] == message)  # Works just like message.

# negative indices also allowed. Counting starts from the end of the string where first index is -1
print(message[-6:-1+1])
print(".................")

print(len(message))
print(message.lower())
print(message.upper())
msg = " Hell yeah!    ---------------------"
print(msg.strip())
my_message = "Pradeep Ramola"
print(my_message.startswith("Pra"))
print(my_message.endswith("gola"))
print(message.count("o", 1, 8))
print(message.find("Python"))
print(my_message.replace("Ramola", "Rana"))
print(my_message)
print(my_message.split())


words = ["Hello", "World", "Python"]
message = " ".join(words)
print(message)   # Output: "Hello World Python"


# ------ Alignment with width

name = "John"
age = 25
profession = "Engineer"

# Aligning values with width
message = "|{:<10}|{:>5}|{:^100}|".format(name, age, profession)
print(message)   # Output: "|John      |   25|"


# -----------------------------
text = """This is a multiline string.
it spans multiple lines.
each line will be capitalized."""

# Splitting the text into lines, capitalizing each line, and then joining them back
lines = text.split("\n")
capitalized_lines = [line.capitalize() for line in lines]
processed_text = "\n".join(capitalized_lines)
print(processed_text)


