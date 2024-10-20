# Max Heap and Min Heap using heapq

import heapq

# Min Heap Example (default in heapq)
min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 5)

print("Min Heap:", min_heap)  # Output: Min Heap: [5, 10, 20, 30]

# Pop element from Min Heap
print("Pop Min:", heapq.heappop(min_heap))  # Output: 5

# Max Heap Example (using negative values to simulate max heap)
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -5)

print("Max Heap:", [-x for x in max_heap])  # Output: Max Heap: [30, 10, 20, 5]

# Pop element from Max Heap
print("Pop Max:", -heapq.heappop(max_heap))  # Output: 30
