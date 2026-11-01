# Binary Search Tree (BST) Program in Python

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    # Insert node
    def insert(self, value):
        if value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)

        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    # Search node
    def search(self, value):
        if value == self.data:
            return True
        elif value < self.data and self.left:
            return self.left.search(value)
        elif value > self.data and self.right:
            return self.right.search(value)
        return False

    # Find minimum value
    def min_value(self):
        current = self
        while current.left:
            current = current.left
        return current.data

    # Delete node
    def delete_node(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)

        else:
            # Node has no children
            if not self.left and not self.right:
                return None

            # Node has only right child
            elif not self.left:
                return self.right

            # Node has only left child
            elif not self.right:
                return self.left

            # Node has two children
            successor = self.right.min_value()
            self.data = successor
            self.right = self.right.delete_node(successor)

        return self

    # Display inorder traversal
    def display(self):
        if self.left:
            self.left.display()
        print(self.data, end=" ")
        if self.right:
            self.right.display()


class BST:
    def __init__(self):
        self.root = None

    # Insert node
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root.insert(value)
        print("Node inserted successfully.")

    # Search node
    def search(self, value):
        if not self.root:
            print("Tree is empty.")
        elif self.root.search(value):
            print(f"Node {value} found in BST.")
        else:
            print(f"Node {value} not found.")

    # Delete node
    def delete_node(self, value):
        if not self.root:
            print("Tree is empty.")
            return

        self.root = self.root.delete_node(value)
        print("Node deleted (if it existed).")

    # Update node
    def update(self, old_value, new_value):
        if not self.root:
            print("Tree is empty.")
            return

        if self.root.search(old_value):
            self.root = self.root.delete_node(old_value)
            self.insert(new_value)
            print("Node updated successfully.")
        else:
            print("Old value not found.")

    # Display BST
    def display(self):
        if not self.root:
            print("Tree is empty.")
        else:
            print("BST elements (Inorder): ", end="")
            self.root.display()
            print()


# Main function
def main():
    tree = BST()

    while True:
        print("\n--- Binary Search Tree Menu ---")
        print("1. Insert Node")
        print("2. Update Node")
        print("3. Delete Node")
        print("4. Search Node")
        print("5. Display BST")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                value = int(input("Enter value to insert: "))
                tree.insert(value)

            elif choice == 2:
                old_value = int(input("Enter old value: "))
                new_value = int(input("Enter new value: "))
                tree.update(old_value, new_value)

            elif choice == 3:
                value = int(input("Enter value to delete: "))
                tree.delete_node(value)

            elif choice == 4:
                value = int(input("Enter value to search: "))
                tree.search(value)

            elif choice == 5:
                tree.display()

            elif choice == 6:
                print("Exiting program...")
                break

            else:
                print("Invalid choice! Try again.")

        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
