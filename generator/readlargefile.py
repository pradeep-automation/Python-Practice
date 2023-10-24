def read_file(file):
    with open(file, "r") as f:

        for line in f:
            yield line
#
for content in read_file("large_file.txt"):
    print(content)


# print(read_file("large_file.txt").__next__())