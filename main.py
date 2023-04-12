from myLib.datastructures.trees.AVL import AVL
from myLib.datastructures.trees.BST import BST
from myLib.datastructures.nodes.TNode import TNode

test = 16
tree = AVL(TNode(10))
tree.insert(11)
tree.insert(12)
tree.insert(100)
tree.insert(15)
tree.insert(16)
tree.insert(9)
tree.insert(17)

tree.print_bf()
print(f"Balance for {test}: {tree.search(test).parent}")