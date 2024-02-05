#Self Balancing Tree

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def preorder(root):
    if not root:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
    if not root:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.data, end=" ")
#LL Rotation
def height(root):
    if root is None:
        return 0
    return root.height


def LLRotation(root):
    new_root=root.left
    root.left=new_root.right
    new_root.right=root
    root.height=max(height(root.left),height(root.right))+1
    new_root.height=max(height(new_root.left),height(new_root.right))+1
    return new_root