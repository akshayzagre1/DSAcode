def hash_function(key, size):
    return key % size

def insert(table, key):
    size = len(table)
    index = hash_function(key, size)
    original_index = index

    while table[index] is not None and table[index] != -1:
        if table[index] == key:
            print("Key already exists")
            return
        index = (index + 1) % size
        if index == original_index:
            print("Hash table is full")
            return
    
    table[index] = key
    print("Key inserted at index", index)

def search(table, key):
    size = len(table)
    index = hash_function(key, size)
    original_index = index

    while table[index] is not None:
        if table[index] == key:
            print("Key found at index", index)
            return index
        index = (index + 1) % size
        if index == original_index:
            break

    print("Key not found.")
    return None

def delete(table, key):
    index = search(table, key)
    if index is not None:
        table[index] = -1
        print("Key deleted.")

def display(table):
    print("Hash Table:")
    for i in range(len(table)):
        print(i, ":", table[i])

def main():
    size = int(input("Enter size of hash table: "))
    table = [None] * size

    while True:
        print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = int(input("Enter key to insert: "))
            insert(table, key)
        elif choice == "2":
            key = int(input("Enter key to search: "))
            search(table, key)
        elif choice == "3":
            key = int(input("Enter key to delete: "))
            delete(table, key)
        elif choice == "4":
            display(table)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
