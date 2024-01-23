#Binary search tree using in order traversal to DLK

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
# def BinaryST_to_DLK(root,prev,head):
#     if root is None:
#         return
#     BinaryST_to_DLK(root.left,prev,head)
#     if head is None:
#         head=root
#         prev=root
#     else:
#         prev.right=root
#         root.left=prev
#         prev=prev.right
#     BinaryST_to_DLK(root.right)
#
#
# def BTToDLL(root):
#     if root is None:
#         return root
#         # Convert to doubly linked
#     # list using BLLToDLLUtil
#     root = BinaryST_to_DLK(root)
#
#     # We need pointer to left most
#     # node which is head of the
#     # constructed Doubly Linked list
#     while root.left:
#         root = root.left
#
#     return root
#
#
# def print_list(head):
#     """Function to print the given
#        doubly linked list"""
#     if head is None:
#         return
#     while head:
#         print(head.data, end=" ")
#         head = head.right

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.right:
            root.data=succesor(root)
            root.right=deleteNode(root.right,root.data)
        else:
            root.data=predecessor(root)
            root.left=deleteNode(root.left,root.data)
    return root

def succesor(root):
    root=root.right
    while root.left is not None:
        root=root.left
    return root.data

def predecessor(root):
    root=root.left
    while root.right is not None:
        root=root.right
    return root.data
mynode=Node(1)
mynode.left=Node(2)
mynode.right=Node(3)
mynode.left.left=Node(4)
mynode.left.right=Node(5)
mynode.right.left=Node(6)
mynode.right.right=Node(7)

print(deleteNode(mynode,5))