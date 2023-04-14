from myLib.datastructures.linear.Queue import LLQueue
from myLib.datastructures.nodes.DNode import DNode
import random

if __name__ == '__main__':
    node = DNode(random.randint(0, 100))
    # Testing Constructors
    linked_list = LLQueue()
    print(f"Intializing queue with a nothing:")
    linked_list.print()

    linked_list = LLQueue(0)
    print(f"Intializing queue with an integer:")
    linked_list.print()

    linked_list  = LLQueue(node)
    print(f"Intializing queue with a node:")
    linked_list.print()

    # Testing enqueue
    print(f"Testing enqueue with 5 random numbers from 0 - 100:")
    for i in range(5):
        linked_list.enqueue(random.randint(0, 100))
    linked_list.print()

    # Testing dequeue
    print(f"Testing dequeue:")
    linked_list.dequeue()
    linked_list.print()

    # Testing Inserts,
    print(f"Testing insert, delete, and sort (Not available with Queue)")
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