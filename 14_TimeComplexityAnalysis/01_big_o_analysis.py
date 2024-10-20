# Big-O Notation and Time Complexity Analysis

# Introduction to Big-O:
# Big-O notation is used to describe the performance or complexity of an algorithm.
# It gives us an upper bound on the time it will take relative to the input size (n).

def constant_time_operation(arr):
    # O(1) - Constant Time
    return arr[0]  # No matter the size of the array, this operation takes the same time.

def linear_time_operation(arr):
    # O(n) - Linear Time
    for item in arr:
        print(item)

def quadratic_time_operation(arr):
    # O(n^2) - Quadratic Time
    for i in arr:
        for j in arr:
            print(i, j)

arr = [1, 2, 3, 4]
print("Constant time operation result:", constant_time_operation(arr))  # O(1)
linear_time_operation(arr)  # O(n)
quadratic_time_operation(arr)  # O(n^2)
