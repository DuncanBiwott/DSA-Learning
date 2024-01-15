# Queue
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class StackA:
    def __init__(self, value):
        self.top = Node(value)
        self.length = 1


    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1
        return self

    def pop(self):
        value_pop = self.top
        if self.length == 0:
            print("Stack is empty")
            return None
        else:
            self.top = self.top.next
            value_pop.next = None
            self.length -= 1
        if self.length == 0:
            self.top = None
        return value_pop.data

    def printstack(self):
        if self.length == 0:
            print("Stack is empty")
            return None
        my_top = self.top
        while my_top is not None:
            print(my_top.data)
            my_top = my_top.next
class StackB:
    def __init__(self, value=None):
        self.top = Node(value)
        self.length = 1

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1
        return self
    def pop(self):
        value_pop = self.top
        if self.length == 0:
            print("Stack is empty")
            return None
        else:
            self.top = self.top.next
            value_pop.next = None
            self.length -= 1
        if self.length == 0:
            self.top = None
        return value_pop.data
    def printstack(self):
        if self.length == 0:
            print("Stack is empty")
            return None
        my_top = self.top
        while my_top is not None:
            print(my_top.data)
            my_top = my_top.next

# class Queue:
#     def __init__(self,value):
#         self.first = None
#         self.last = None
#         self.length = 0
#         self.stackA = StackA(value)
#         self.stackB = StackB(value)
#     def enqueue(self):
#         top_stackA = self.stackA.top
#         if self.length == 0:
#             self.first=top_stackA
#             self.last = top_stackA
#         else:
#             self.last.next = top_stackA
#             self.last = top_stackA
#         self.length += 1
#         return self
#     def dequeue(self):
#         if self.length == 0:
#             return None
#         if self.length == 1:
#             self.last = None
#             self.stackB = StackB(self.first.value)
#         first_pop= self.first
#         to_stackB = StackB(first_pop.value).push(first_pop.value)
#         self.first = self.first.next
#         first_pop.next = None
#         self.length -= 1
#         return self
#     def peek(self):
#         return self.first
#     def printqueue(self):
#         my_first = self.first
#         while my_first is not None:
#             print(my_first.value)
#             my_first = my_first.next
#         return self

def queueFrom2Stacks(stackA):

    if stackA.length == 0:
        print("Stacks are empty")
        return None
    stackB = StackB()
    while stackA.length > 0:
        stackB.push(stackA.pop())
    return stackB

def enqueue(stackA):
    stackB=queueFrom2Stacks(stackA)
    top_stackB = stackB.top
    enqueued=[]
    while top_stackB.next:
        print(top_stackB.data)
        enqueued.append(top_stackB.data)
        top_stackB = top_stackB.next
    return enqueued




stackA = StackA(5)
stackA.push(10)
stackA.push(15)
stackA.push(20)
stackA.printstack()
print("**********")
print(enqueue(stackA))