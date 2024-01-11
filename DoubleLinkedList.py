class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self,value):
       newNode=Node(value)
       self.head=newNode
       self.tail=newNode
       self.length=1
    def append(self,value):
        newNode=Node(value)
        if self.length==0:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
        self.length+=1
        return self
    def prepend(self,value):
        newNode=Node(value)
        if self.length==0:
            self.head=newNode
            self.tail=newNode
        else:
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
        self.length+=1
        return self
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def get(self,index):
        mynode=self.head
        if index < 0 or index >=self.length:
            return None
        for _ in range(index):
                mynode=mynode.next
        return mynode

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
mydouble=DoubleLinkedList(1)
mydouble.append(2)
mydouble.append(3)
mydouble.append(4)
mydouble.append(5)
print(mydouble.printList())
mydouble.set_value(1,6)
mydouble.get(1)
mydouble.printList()
mydouble.pop_first()
mydouble.printList()