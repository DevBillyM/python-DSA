# Hash Map Implementation using Python's dict

# Create a hash map using dict
hash_map = {}

# Insert key-value pairs
hash_map["name"] = "John"
hash_map["age"] = 30
hash_map["city"] = "New York"

# Access elements
print("Name:", hash_map.get("name"))  # Output: John
print("Age:", hash_map.get("age"))  # Output: 30

# Modify a value
hash_map["age"] = 31
print("Updated Age:", hash_map.get("age"))  # Output: 31

# Delete a key-value pair
del hash_map["city"]
print("Hash Map after deletion:", hash_map)  # Output: {'name': 'John', 'age': 31}

# Iterate through the hash map
for key, value in hash_map.items():
    print(f"{key}: {value}")
