# List Operations in Python

# List creation
my_list = [10, 20, 30, 40]

# Access elements
print("First element:", my_list[0])  # Output: 10
print("Last element:", my_list[-1])  # Output: 40 (Negative index accesses elements from the end)

# Modify elements
my_list[2] = 35
print("After modification:", my_list)  # Output: [10, 20, 35, 40]

# Add elements
my_list.append(50)
print("After appending:", my_list)  # Output: [10, 20, 35, 40, 50]

# Remove elements
my_list.remove(20)
print("After removal:", my_list)  # Output: [10, 35, 40, 50]

# Length of the list
print("Length of the list:", len(my_list))  # Output: 4
