class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
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


def reverse_string(string):
    reverse_string = ""
    stack = Stack(string[0])
    for i in range(1, len(string)):
        stack.push(string[i])
    for i in range(stack.height):
        reverse_string += stack.pop()
    return reverse_string

def reverse_words(string):
    splitted = string.split(" ")
    for i in range(len(splitted)):
        splitted[i] = reverse_string(splitted[i])
    print(" ".join(splitted))

test_String = "I am Learning Data Structures and Algorithms"
print(reverse_string(test_String))
reverse_words(test_String)
