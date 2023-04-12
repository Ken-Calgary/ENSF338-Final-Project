
from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.trees.BST import BST

class AVL(BST):
    def __init__(self, data=None):
        def traverse(node):
            if not node:
                return

            traverse(node.left)
            self.insert(node.data)
            traverse(node.right)
        
        if isinstance(data, int):
            super().__init__(data)
            self.root = self._balance(self.root)
        else:
            super().__init__(None)
            traverse(data)
            

    def __repr__(self):
        return self.root.__repr__()

    def insert(self, data):
        def _insert(node, data):
            if isinstance(data, int):
                if node is None:
                    return TNode(data)
                elif data < node.data:
                    node.left = _insert(node.left, data)
                else:
                    node.right = _insert(node.right, data)

                node = self._balance(node)
                return node
            else:
                if node is None:
                    return TNode(data)
                elif data.data < node.data:
                    node.left = _insert(node.left, data.data)
                else:
                    node.right = _insert(node.right, data.data)

                node = self._balance(node)
                return node
        self.root = _insert(self.root, data)

    def delete(self, data):
        def _find_min(self, node):
            while node.left is not None:
                node = node.left
            return node
        def _delete(node, data):
            if node is None:
                return None
            elif data < node.data:
                node.left = _delete(node.left, data)
            elif data > node.data:
                node.right = _delete(node.right, data)
            else:
                if node.left is None and node.right is None:
                    node = None
                elif node.left is None:
                    node = node.right
                elif node.right is None:
                    node = node.left
                else:
                    min_node = _find_min(node.right)
                    node.data = min_node.data
                    node.right = _delete(node.right, min_node.data)

            if node is not None:
                node = self._balance(node)
            return node
        self.root = _delete(self.root, data)

    def _balance(self, node):
        def _get_height( node):
            if node is None:
                return 0
            return 1 + max(_get_height(node.left), _get_height(node.right))

        def _get_balance( node):
            if node is None:
                return 0
            return _get_height(node.left) - _get_height(node.right)

        def _calc_balance(node):
            if node is None:
                return 0
            return 1 + max(_calc_balance(node.left), _calc_balance(node.right))

        # helper
        def _rotate_left(node):
            new_root = node.right
            node.right = new_root.left
            new_root.left = node
            node.balance = _calc_balance(node)
            new_root.balance = _calc_balance(new_root)
            return new_root

        # helper
        def _rotate_right( node):
            new_root = node.left
            node.left = new_root.right
            new_root.right = node
            node.balance = _calc_balance(node)
            new_root.balance = _calc_balance(new_root)
            return new_root

        if node is None:
            return None

        if _get_balance(node) > 1:
            if  _get_balance(node.left) < 0:
                node.left = _rotate_left(node.left)
            node = _rotate_right(node)
        elif _get_balance(node) < -1:
            if _get_balance(node.right) > 0:
                node.right = _rotate_right(node.right)
            node = _rotate_left(node)

        node.balance = _calc_balance(node)
        return node