message = "Hello Python!"
# # Indexing
# print(message[7])
# print(message[11])
# print(message.index("Py"))
#
# # Slicing -- Starting index is inclusive and end index is exclusive
#
# print(message[0:4])
# print(message[4:8])
#
# """You can omit the start index in slicing to start from the beginning of the string,
# and omit the end index to slice until the end of the string:
# """
# print(message[:5])
# print(message[2:])
# print(message[:] == message)  # Works just like message.
# # negative indices also allowed. Counting starts from the end of the string where first index is -1
print(message[::-1],"my mesaage")
m = reversed(message)
print()
# print(".................")
#
# print(len(message))
# print(message.lower())
# print(message.upper())
# msg = " Hell yeah!    ---------------------    "
# print(msg.rstrip())
# my_message = ["Pradeep Ramola", "Prashant", "Dinesh", "Prem"]
# # if my_message.startswith("Pra"):
# for msg in my_message:
#     if msg.startswith("Pra"):
#         print(msg)
# message = "Hello Python!"
# print(message.count("o", 1, len(message)))
# print(message.find("Python"))
# print(my_message.replace("Ramola", "Rana"))
# my_message = "Pradeep Ramola"
# print(my_message)
# print(my_message.split())
#
#
# words = ["Hello", "World", "Python"]
# message = " ".join(words)
# print(message)   # Output: "Hello World Python"

# ------ Alignment with width

# name = "John"
# age = 25
# profession = "Engineer"
#
# # Aligning values with width
# # message = "|{:<10}|{:>5}|{:^100}|".format(name, age, profession)
# message = f"|{name:<5}|{age:>5}|{profession:^10}|"
# print(message)   # Output: "|John      |   25|"
#
#
# -----------------------------
text = """This is a multiline string.
it spans mUltiple lines.
each line will be capitalized."""

# Splitting the text into lines, capitalizing each line, and then joining them back
lines = text.splitlines()
print(lines)
capitalized_lines = [line.capitalize() for line in lines]
processed_text = "\n".join(capitalized_lines)
print(processed_text)


