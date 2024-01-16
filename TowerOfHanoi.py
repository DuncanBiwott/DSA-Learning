# Implementing tower of hanoi using stacks as rods
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackSource:
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


class StackMiddle:
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


class StackDestination:
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
            return
        my_top = self.top
        while my_top is not None:
            print(my_top.data)
            my_top = my_top.next


class StackSource:
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
            return
        else:
            self.top = self.top.next
            value_pop.next = None
            self.length -= 1
        if self.length == 0:
            self.top = None
        return value_pop.data

    def printstack(self):
        if self.length == 0:
            return
        my_top = self.top
        while my_top is not None:
            print(my_top.data)
            my_top = my_top.next


def tower_of_hanoi(n, stackSource, stackDestination, stackMiddle):
    if n == 1:
        stackDestination.push(stackSource.pop())
    else:
        tower_of_hanoi(n - 1, stackSource, stackMiddle, stackDestination)
        stackDestination.push(stackSource.pop())
        tower_of_hanoi(n - 1, stackMiddle, stackDestination, stackSource)


# Using loops instead of recursion
def tower_of_hanoi2(n, stackSource, stackDestination, stackMiddle):
    shifting_steps = int(pow(2, n) - 1)
    for i in range(shifting_steps -1):
        if i % 3 == 0:
            to_move_val = stackMiddle.pop()
            stackDestination.push(to_move_val)
        if i % 3 == 1:
            from_source = stackSource.pop()
            stackDestination.push(from_source)

        if i % 3 == 2:
            from_middle = stackSource.pop()
            stackMiddle.push(from_middle)
    return stackDestination.printstack()


stackSource = StackSource(5)
stackSource.push(4)
stackSource.push(3)
stackMiddle = StackMiddle()
stackDestination = StackDestination()

tower_of_hanoi2(3, stackSource, stackDestination, stackMiddle)