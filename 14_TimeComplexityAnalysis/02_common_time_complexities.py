# Examples of Common Time Complexities

import math

def constant_time_example(n):
    # O(1) - Constant Time
    return n * 2  # Single operation, independent of input size.

def logarithmic_time_example(n):
    # O(log n) - Logarithmic Time
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count

def linear_time_example(arr):
    # O(n) - Linear Time
    for i in arr:
        print(i)

def linear_logarithmic_time_example(arr):
    # O(n log n) - Linearithmic Time (e.g., sorting algorithms like Merge Sort, Quick Sort)
    arr.sort()
    print("Sorted array:", arr)

def quadratic_time_example(n):
    # O(n^2) - Quadratic Time (e.g., nested loops)
    for i in range(n):
        for j in range(n):
            print(i, j)

# Testing Different Time Complexities
n = 16
arr = [3, 1, 4, 1, 5, 9, 2, 6]

print("Constant Time (O(1)):", constant_time_example(n))  # Output: 32
print("Logarithmic Time (O(log n)):", logarithmic_time_example(n))  # Output: 4
print("Linear Time (O(n)):")
linear_time_example(arr)  # Output: Prints each element of arr
print("Linearithmic Time (O(n log n)):")
linear_logarithmic_time_example(arr)  # Output: Sorted array
print("Quadratic Time (O(n^2)):")
quadratic_time_example(3)  # Output: Nested loop prints combinations
