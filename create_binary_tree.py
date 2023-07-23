from IPython.display import Markdown
from IPython.display import display_markdown

def create_binary_tree(input_list, index):
    if index >= len(input_list) or input_list[index] is None:
        return None

    node = {"data": input_list[index], "left": None, "right": None}
    node["left"] = create_binary_tree(input_list, 2 * index + 1)
    node["right"] = create_binary_tree(input_list, 2 * index + 2)
    return node

# Example binary tree represented as a list
binary_tree_list = [1, 2, 3, 4, 5, 6, 7]

# Create the binary tree using the list
root = create_binary_tree(binary_tree_list, 0)
print(root)