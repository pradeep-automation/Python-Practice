def read_file(file):
    with open(file, "r") as f:

        for line in f:
            yield line


gen = read_file("large_file.txt")

for content in read_file("large_file.txt"):
    print(content, end="")


# print(read_file("large_file.txt").__next__())