class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    def printstack(self):
        my_top = self.top
        while my_top is not None:
            print(my_top.value)
            my_top = my_top.next
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        value_pop = self.top
        if self.height == 0:
            print("Stack is empty")
            return None
        else:
            self.top = self.top.next
            value_pop.next = None
            self.height -= 1
        if self.height == 0:
            self.top = None
        return value_pop.value
stack= Stack(5)
stack.push(10)
stack.push(15)
stack.push(20)

print(stack.pop())
stack.push(25)
print(stack.pop())

