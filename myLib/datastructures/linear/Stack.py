# Implemntation of Stack
from SLL import SLL
from myLib.datastructures.nodes.DNode import DNode
import random


class Stack(SLL):
    def __init__(self, head=None):
        super().__init__(head)

    def push(self, node):
        super().insert_head(node)
    
    def insert_head(self, node):
        return
    
    def insert_tail(self, node):
        return
    
    def peek(self):
        return self.head.data
    
    def pop(self):
        head = self.head
        super().delete_head()
        return head
    
    def delete_head(self):
        return
    
    def delete_tail(self):
        return
    
    def sort(self):
        return
    
    def sorted_insert(self, node):
        return 