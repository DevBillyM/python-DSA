# Circular Queue Implementation

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full"

        elif self.front == -1:  # First element
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:  # Queue is empty
            return "Queue is empty"

        elif self.front == self.rear:  # Only one element
            data = self.queue[self.front]
            self.front = self.rear = -1
            return data
        else:
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return data

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.rear >= self.front:
            print("Queue:", self.queue[self.front : self.rear + 1])
        else:
            print("Queue:", self.queue[self.front:] + self.queue[:self.rear + 1])

# Testing Circular Queue
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()  # Output: [10, 20, 30]
cq.dequeue()
cq.display()  # Output: [20, 30]
