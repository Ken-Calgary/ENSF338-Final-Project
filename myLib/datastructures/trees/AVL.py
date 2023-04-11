# Implemntation of AVL (Self-balancing binary search tree)
from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.trees.BST import BST

class AVL(BST):
    def __init__(self, data=None):
        super().__init__(data)
        self.root = self._balance(self.root)

    def __repr__(self):
        return self.root.__repr__()

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if isinstance(data, int):
            if node is None:
                return TNode(data)
            elif data < node.data:
                node.left = self._insert(node.left, data)
            else:
                node.right = self._insert(node.right, data)

            node = self._balance(node)
            return node
        else:
            if node is None:
                return TNode(data)
            elif data.data < node.data:
                node.left = self._insert(node.left, data.data)
            else:
                node.right = self._insert(node.right, data.data)

            node = self._balance(node)
            return node

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None
        elif data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                min_node = self._find_min(node.right)
                node.data = min_node.data
                node.right = self._delete(node.right, min_node.data)

        if node is not None:
            node = self._balance(node)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _balance(self, node):
        if node is None:
            return None

        if self._get_balance(node) > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        elif self._get_balance(node) < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)

        node.balance = self._calc_balance(node)
        return node

    def _get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _calc_balance(self, node):
        if node is None:
            return 0
        return 1 + max(self._calc_balance(node.left), self._calc_balance(node.right))

    # helper
    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.balance = self._calc_balance(node)
        new_root.balance = self._calc_balance(new_root)
        return new_root

    # helper
    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.balance = self._calc_balance(node)
        new_root.balance = self._calc_balance(new_root)
        return new_root