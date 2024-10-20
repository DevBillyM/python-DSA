# Custom Hash Map with Collision Handling using Separate Chaining

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Handle collisions by appending to the list at the hashed index
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value  # Update if key exists
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return "Key not found"

    def delete(self, key):
        index = self.hash_function(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return "Key deleted"
        return "Key not found"

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Testing Custom Hash Map
ht = HashTable()
ht.insert("name", "John")
ht.insert("age", 30)
ht.insert("city", "New York")
ht.display()

print("Search for 'name':", ht.search("name"))  # Output: John
print("Search for 'city':", ht.search("city"))  # Output: New York

ht.delete("city")
ht.display()  # Output: 'city' should be deleted
