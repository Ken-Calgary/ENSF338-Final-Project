# Implemntation of Stack
from myLib.datastructures.linear.SLL import SLL

class Stack(SLL):
    def __init__(self, head=None):
        super().__init__(head)

    def push(self, node):
        super().insert_head(node)
    
    def insert_tail(self, node):
        return
    
    def peek(self):
        return self.head.data
    
    def pop(self):
        head = self.head
        super().delete_head()
        return head
    
    def delete_tail(self):
        return
    