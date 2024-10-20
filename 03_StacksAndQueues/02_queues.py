# Queue Implementation using collections.deque

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Testing Queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue:", list(queue.queue))  # Output: [10, 20, 30]
queue.dequeue()
print("Queue after dequeue:", list(queue.queue))  # Output: [20, 30]
