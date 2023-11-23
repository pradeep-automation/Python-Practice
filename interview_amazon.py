# # Python program to reverse a linked list
# # Time Complexity : O(n)
# # Space Complexity : O(1)
#
# # Node class
# class Node:
#     # Constructor to initialize the node object
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#
#     # Function to reverse the linked list
#     def reverse(self):
#         prev = None
#         current = self.head
#         while (current is not None):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev
#
#     # Function to insert a new node at the beginning
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     # Utility function to print the LinkedList
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data, end=" ")
#             temp = temp.next
#
#
# # Driver code
# llist = LinkedList()
# llist.push(20)
# llist.push(4)
# llist.push(15)
# llist.push(85)
#
# print("Given linked list")
# llist.printList()
# llist.reverse()
# print("\nReversed linked list")
# llist.printList()


import random

# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Function to reverse the linked list
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# Create a linked list with 20 random integers
head = Node(random.randint(1, 100))
current = head
for _ in range(19):
    current.next = Node(random.randint(1, 100))
    current = current.next

# Print the original linked list
print("Original Linked List:")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("\nReversed Linked List:")
print_linked_list(head)
