#Binary Search Tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def search(self, key):
        if key < self.data:
            if self.left is None:
                return str(key) + " Not Found"
            return self.left.search(key)
        elif key > self.data:
            if self.right is None:
                return str(key) + " Not Found"
            return self.right.search(key)
        else:
            print(str(self.data) + ' is found')

        # Insert method to create nodes

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    # A function to do inorder tree traversal
    # def printInorder(root):
    #
    #     if root:
    #         # First recur on left child
    #         printInorder(root.left)
    #
    #         # Then print the data of node
    #         print(root.val, end=" "),
    #
    #         # Now recur on right child
    #         printInorder(root.right)

    def inorder(self):
        if self.left:
            self.left.inorder()
            print(self.data, "->", end=" ")
        if self.right:
            self.right.inorder()
    def deleteNode(self, key):
        if self is None:
            return None
        if key < self.data:
            self.left = self.left.deleteNode(key)
        elif key > self.data:
            self.right = self.right.deleteNode(key)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right:
                self.data = self.succesor()
                self.right = self.right.deleteNode(self.data)
            else:
                self.data = self.predecessor()
                self.left = self.left.deleteNode(self.data)
        return self




root = Node(54)
root.insert(55)
root.insert(46)
root.insert(12)
root.insert(23)
root.insert(5)
root.inorder()


