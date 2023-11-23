import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list():
    head = Node(random.randint(1, 100))
    current = head
    n = 1
    print("Linked List is ---->")
    while n<=20:
        print(current.data, end='->')
        current.next = Node(random.randint(1, 100))
        current = current.next
        n += 1
    print("None")

    print("Reversed Linked List is ---->")

    # while current:
    #     print(current.data, end='->')
    #     current = current.next
    # print("None")


# creating linked list with 20 random integers
# h = Node(random.randint(1, 100))
# c = h
#
# for i in range(19):
#     c.next = Node(random.randint(1, 100))
#     c = c.next

print_linked_list()



