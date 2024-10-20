# Doubly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, key):
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            return

        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next

        if temp is None:
            return

        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Testing Doubly Linked List
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.traverse()  # Output: 10 <-> 20 <-> 30 <-> None
dll.delete_node(20)
dll.traverse()  # Output: 10 <-> 30 <-> None
