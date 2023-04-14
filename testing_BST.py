from myLib.datastructures.trees.BST import BST
from myLib.datastructures.nodes.TNode import TNode
import random

if __name__ == '__main__':

    # Testing Constructors
    tree = BST()
    print(f"Intializing Binary Search Tree with a nothing:", end = " ")
    tree.print_bf()

    tree = BST(random.randint(0,100))
    print(f"Intializing Binary Search Tree with an integer:", end = " ")
    tree.print_bf()

    tree  = BST(TNode(50))
    print(f"Intializing Binary Search Tree with a node (constant 50, changable):", end =" ")
    tree.print_bf()

    # Testing out insert for numbers less than root
    print("Testing insert with integer for number less than 50")
    tree.insert(random.randint(0,49))
    tree.insert(TNode(random.randint(0,49)))
    tree.print_bf()

    # Testing out insert for numbers greater than 50
    num = random.randint(51,100) # Saving this number, as delete uses an integer
    print("Testing insert with integer for numbers greater than 50:")
    tree.insert(random.randint(51, 100))
    tree.insert(num)
    tree.print_bf()

    # Testing delete
    print(f"Testing delete of {num}: ")
    tree.delete(num)
    tree.print_bf()

    # Testing Root getter and setter
    print("Testing getter and setter:")
    set_tree = BST()
    for i in range(5):
        num = random.randint(0,100)
        set_tree.insert(num)

    print(f"The tree we're setting: ")
    set_tree.print_bf() 

    print(f"Setting the original tree to the tree we're setting")
    tree.set_root(set_tree.get_root())
    tree.print_bf()

    # Testing search
    print(f"Testing search with {num}:")
    print(f"Existing number: {tree.search(num)}")
    print(f"Non-existing number in tree: {tree.search(1000)}\n")

    #Testing print in order
    print("Testing printing in order:")
    tree.print_in_order()