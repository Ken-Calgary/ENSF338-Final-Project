class SSL:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        if self.head is not None:
            current = self.head
            while current is not None:
                self.tail = current
                current = current.next

            self.size += 1

    def InsertHead(self, node):
        node.next = self.head
        self.head = node
        self.size += 1
        if self.size == 1:
            self.tail = node

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def Insert(self, node, position):
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")
        if position == 0:
            self.InsertHead(node)
        elif position == self.size:
            self.InsertTail(node)
        else:
            prev_node = self.get_node(position - 1)
            node.next = prev_node.next
            prev_node.next = node
            self.size += 1

    def SortedInsert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1

        else:
            current = self.head
            # sorts the linkedlist if not already sorted
            while current is not None and current.next is not None:
                if current.data > current.next.data:
                    self.Sort()
                    break
                current = current.next
            
            if node.data < self.head.data:
                self.InsertHead(node)
            elif node.data > self.tail.data:
                self.InsertTail(node)
            else:
                current = self.head
                while current.next is not None and node.data > current.next.data:
                    current = current.next
                node.next = current.next

                current.next = node
                self.size += 1

    def Search(self, node):
        current_node = self.head
        while current_node:
            if current_node.data == node.data:
                return current_node
            current_node = current_node.next
        return None

    def DeleteHead(self):
        if not self.head:
            return
        self.head = self.head.next
        self.size -= 1
        if not self.head:
            self.tail = None

    def DeleteTail(self):
        if not self.head:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node
        self.size -= 1

    def Delete(self, node):
        if not self.head:
            return
        if self.head.data == node.data:
            self.DeleteHead()
            return
        current_node = self.head.next
        prev_node = self.head
        while current_node:
            if current_node.data == node.data:
                prev_node.next = current_node.next
                self.size -= 1
                if current_node == self.tail:
                    self.tail = prev_node
                return
            prev_node = current_node
            current_node = current_node.next

    def Sort(self):
        if not self.head or not self.head.next:
            return
    
        sorted_list = None
        current = self.head
        while current:
            node = current
            current = current.next

            if not sorted_list or node.data <= sorted_list.data:
                node.next = sorted_list
                sorted_list = node
            else:
                current_sorted = sorted_list
                while current_sorted.next and current_sorted.next.data < node.data:
                    current_sorted = current_sorted.next

                node.next = current_sorted.next
                current_sorted.next = node
            self.head = sorted_list
            while self.tail.next:
                self.tail = self.tail.next
    
    def Clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        print("List Size: " ,self.size)
        
        current = self.head
        sorted = True
        while current is not None and current.next is not None:
            if current.data > current.next.data:
                print("Sorted Status: Not Sorted")
                sorted = False
                break
            current = current.next

        if (sorted and self.size != 0):
            print("Sort Status: Sorted")
        
        current = self.head
        print("Content List: ", end = " ")
        while current is not None:
            print(current.data, end = " ")
            current = current.next
        
