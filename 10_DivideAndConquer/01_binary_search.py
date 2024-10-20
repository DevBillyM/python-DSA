# Binary Search Implementation using Divide and Conquer

def binary_search(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)

    return -1

# Testing Binary Search
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
