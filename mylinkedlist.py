import random
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end= "->")
        current = current.next
    print("None")

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def find_middle():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    hare = head
    tortoise = head

    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
    return tortoise




h = Node(random.randint(1, 100))
c = h
for i in range(19):
    print(c.data, end = "->")
    c.next = Node(random.randint(1, 100))
    c = c.next
print(None)


print_linked_list(h)
head = reverse_linked_list(h)
print_linked_list(head)

print(find_middle())

