# Circular Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head

    def delete_node(self, key):
        if self.head is None:
            return

        temp = self.head

        if temp.data == key:
            if temp.next == self.head:
                self.head = None
                return
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = self.head.next
            self.head = self.head.next
            return

        prev = None
        while temp.next != self.head:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp.data != key:
            return

        prev.next = temp.next

    def traverse(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Back to Head")

# Testing Circular Linked List
cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.traverse()  # Output: 10 -> 20 -> 30 -> Back to Head
cll.delete_node(20)
cll.traverse()  # Output: 10 -> 30 -> Back to Head
