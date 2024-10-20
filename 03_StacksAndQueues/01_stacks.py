# Stack Implementation using Python list

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Testing Stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack:", stack.stack)  # Output: [10, 20, 30]
print("Top element:", stack.peek())  # Output: 30
stack.pop()
print("Stack after pop:", stack.stack)  # Output: [10, 20]
