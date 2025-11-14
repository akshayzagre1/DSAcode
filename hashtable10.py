# Hash Table Implementation using Chaining

# Create a hash table with 10 empty lists
table = [[] for _ in range(10)]

# Hash function using division method
def hash_function(key):
    return key % 10

# Insert a key into the hash table
def insert(key):
    index = hash_function(key)
    if key not in table[index]:
        table[index].append(key)

# Search for a key in the hash table
def search(key):
    index = hash_function(key)
    return key in table[index]

# Delete a key from the hash table
def delete(key):
    index = hash_function(key)
    if key in table[index]:
        table[index].remove(key)

# Display the contents of the hash table
def display():
    for i in range(10):
        print(f"Index {i}: {table[i]}")

# Example usage
insert(10)
insert(20)
insert(44)
insert(15)
insert(58)
insert(25)

print("\nHash Table after insertions:")
display()

print("\nSearching for keys:")
print("15 found?", search(15))
print("100 found?", search(100))

delete(15)
delete(58)

print("\nHash Table after deletions:")
display()
