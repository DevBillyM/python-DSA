# Heap Sort Implementation using heapq

import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr

# Testing Heap Sort
arr = [12, 3, 5, 7, 19]
print("Original Array:", arr)  # Output: [12, 3, 5, 7, 19]
sorted_arr = heap_sort(arr[:])
print("Heap Sorted Array:", sorted_arr)  # Output: [3, 5, 7, 12, 19]
