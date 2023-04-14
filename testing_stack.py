from myLib.datastructures.linear.Stack import Stack
from myLib.datastructures.nodes.DNode import DNode
import random

if __name__ == '__main__':
    node = DNode(50)
    # Testing Constructors
    linked_list = Stack()
    print(f"Intializing CircularDoublyLL with a nothing:")
    linked_list.print()

    linked_list = Stack(0)
    print(f"Intializing CircularDoublyLL with an integer:")
    linked_list.print()

    linked_list  = Stack(node)
    print(f"Intializing CircularDoublyLL with a node:")
    linked_list.print()

    print(f"Testing push 5 times:")
    for i in range(5):
        linked_list.push(random.randint(0, 100))
    linked_list.print()

    print(f"Testing pop:")
    linked_list.pop()
    linked_list.print()

    print(f"Testing peek:")
    print(linked_list.peek(), "\n")

    # Testing Inserts,
    print(f"Testing insert, delete, and sort (Not available with Stack)")
    linked_list.insert_head(DNode(random.randint(0, 100)))
    linked_list.insert_tail(DNode(random.randint(0, 100)))
    linked_list.insert(DNode(random.randint(0, 100)), 2)
    linked_list.sort()
    linked_list.delete_head()
    linked_list.delete_tail()
    linked_list.delete(node)

    for i in range (5):
        i = random.randint(0, 100)
        linked_list.sorted_insert(DNode(i))
    linked_list.print()

    print(f"Testing Clear:")
    linked_list.clear()
    linked_list.print()