from myLib.datastructures.linear.DLL import DoublyLL
from myLib.datastructures.nodes.DNode import DNode
import random

if __name__ == '__main__':
    node = DNode(1)
    # Testing Constructors
    linked_list = DoublyLL()
    print(f"Intializing DLL with a nothing:")
    linked_list.print()

    linked_list = DoublyLL(0)
    print(f"Intializing DLL with an integer:")
    linked_list.print()

    linked_list  = DoublyLL(node)
    print(f"Intializing DLL with a node:")
    linked_list.print()

    # Testing Inserts
    print(f"Testing insert head and tail with data from 0 - 100:")
    linked_list.insert_head(DNode(random.randint(0, 100)))
    linked_list.insert_tail(DNode(random.randint(0, 100)))

    linked_list.print()

    print(f"Testing insert with specify position with node data from 0 - 100:")
    linked_list.insert(DNode(random.randint(0, 100)), 2)
    linked_list.print()

    # Testing Sort
    print(f"Testing Sort")
    linked_list.sort()
    linked_list.print()

    # Testing Delete
    print(f"Testing delete with head and tail:")
    linked_list.delete_head()
    linked_list.delete_tail()
    linked_list.print()

    print(f"Testing delete with node specified (This will delete depending if the initialized node\n", 
          "was not a head or tail as it might've been deleted earlier):")
    linked_list.delete(node)
    linked_list.print()

    print(f"Testing SortedInsert:")
    for i in range (5):
        i = random.randint(0, 100)
        linked_list.sorted_insert(DNode(i))
    linked_list.print()

    print(f"Testing Clear:")
    linked_list.clear()
    linked_list.print()