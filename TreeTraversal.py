class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


root= Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(20)
root.right.right=Node(30)

inorder(root)


#Pre-Oreder Traversal

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)