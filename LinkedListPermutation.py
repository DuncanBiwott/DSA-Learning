class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#Find permutation in the linked list
class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self
    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    def find_permutation(self,permutation):
        if self.length==0:
            return False
        temp=self.head
        permuted_list=[]
        for i in range(self.length):
            sub_list = [temp.value]
            if temp.value==permutation[0]:
                for j in range(1,len(permutation)):
                    temp=temp.next
                    if temp.value==permutation[j]:
                        sub_list.append(temp.value)
                    else:
                        return False
                return sub_list
            temp=temp.next
            permuted_list.extend(sub_list)
        return permuted_list

mylinkedlist=LinkedList(10)
mylinkedlist.append(5)
mylinkedlist.append(16)
mylinkedlist.append(20)
permutation=[]
for i in range(mylinkedlist.length):
    permutation.append(mylinkedlist.get(i))
print(mylinkedlist.find_permutation(permutation))