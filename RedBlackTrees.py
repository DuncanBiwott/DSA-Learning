#Red Black Trees

class Color:
    RED = 1
    BLACK = 0
class Node:
    def __init__(self,data,parent,color=Color.RED):
        self.data = data
        self.left = None
        self.right = None
        self.color = color
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.root = None

