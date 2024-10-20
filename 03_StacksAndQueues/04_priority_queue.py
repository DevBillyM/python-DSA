# Priority Queue using heapq

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        heapq.heapify(self.queue)

    def enqueue(self, data):
        heapq.heappush(self.queue, data)

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)
        return "Priority Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

# Testing Priority Queue
pq = PriorityQueue()
pq.enqueue(30)
pq.enqueue(10)
pq.enqueue(20)
print("Priority Queue:", pq.queue)  # Output: [10, 30, 20] (heap structure)
pq.dequeue()
print("Priority Queue after dequeue:", pq.queue)  # Output: [20, 30]
