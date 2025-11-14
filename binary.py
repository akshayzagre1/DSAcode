# Implementation of Binary Search Tree (BST)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    # Search for a node
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Find minimum value node (for deletion)
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Delete a node
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    # Inorder Traversal (Display)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


# ---- Main Program ----
tree = BST()
root = None

# Insert nodes
root = tree.insert(root, 50)
root = tree.insert(root, 30)
root = tree.insert(root, 70)
root = tree.insert(root, 20)
root = tree.insert(root, 40)
root = tree.insert(root, 60)
root = tree.insert(root, 80)

print("BST Inorder Traversal (Sorted): ", end="")
tree.inorder(root)

# Search operation
key = 40
result = tree.search(root, key)
if result:
    print(f"\nKey {key} found in BST")
else:
    print(f"\nKey {key} not found in BST")

# Delete operation
root = tree.delete(root, 70)
print("\nBST after deleting 70:")
tree.inorder(root)
