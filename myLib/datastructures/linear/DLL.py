# Implementation of DoublyLinkedList

from myLib.datastructures.nodes.DNode import DNode
import random

class SinglyLL():

    def __init__(self, node):
        self.head = node

class DoublyLL(SinglyLL):

    def __init__(self, node=None):
        super().__init__(node)
        self.tail = node

    def insert_head(self, node):
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        else:
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
                if not current_node:
                    return
            node.prev = current_node
            node.next = current_node.next
            current_node.next = node
            if node.next:
                node.next.prev = node
            else:
                self.tail = node

    def sorted_insert(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            if not self.isSorted():
                self.sort()

            if new_node.data <= self.head.data:
                new_node.next = self.head
                self.head = new_node
            else:
                current_node = self.head
                while current_node.next and current_node.next.data <= new_node.data:
                    current_node = current_node.next
                new_node.next = current_node.next
                current_node.next = new_node

    # should be inherited
    def search(self, node):
        current_node = self.head
        while current_node and current_node != node:
            current_node = current_node.next
        return current_node

    def delete_head(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # should be inherited
    def delete_tail(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete(self, node):
        if not node:
            return
        if node == self.head:
            self.delete_head()
        elif node == self.tail:
            self.delete_tail()
        elif self.search(node) is not None:
            node.prev.next = node.next
            node.next.prev = node.prev

    def sort(self):
        # If list is empty or only one element, it is already sorted
        if self.head is None or self.head.next is None:
            return
        
        # Traverse the list starting from the second node
        current_node = self.head.next
        while current_node is not None:
            # Get the value of the current node and save the next node
            current_value = current_node.data
            next_node = current_node.next
            
            # Find the node to insert the current node after
            insert_node = current_node.prev
            while insert_node is not None and insert_node.data > current_value:
                insert_node = insert_node.prev
                
            # If current node is already in the correct position, move to next node
            if insert_node is not None and insert_node.next == current_node:
                current_node = next_node
                continue
            
            # Remove the current node from its current position
            current_node.prev.next = current_node.next
            if current_node.next is not None:
                current_node.next.prev = current_node.prev
            
            # Insert the current node after the insert node
            current_node.prev = insert_node
            if insert_node is not None:
                current_node.next = insert_node.next
                insert_node.next.prev = current_node
                insert_node.next = current_node
            else:
                current_node.next = self.head
                self.head.prev = current_node
                self.head = current_node
            
            # Move to next node
            current_node = next_node

    # should be inherited
    def clear(self):
        self.head = None
        self.tail = None

    # should be inherited
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    # should be inherited
    def isSorted(self):
            if not self.head or not self.head.next:
                return True

            current_node = self.head
            while current_node.next:
                if current_node.data > current_node.next.data:
                    return False
                current_node = current_node.next

            return True
