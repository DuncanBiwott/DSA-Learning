#First In First Out (FIFO) Queue-
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,value):
        newVal=Node(value)
        self.first=newVal
        self.last=newVal
        self.length=1

    def enqueue(self,value):
        newVal=Node(value)
        if self.length==0:
            self.first=newVal
            self.last=newVal
        else:
            self.last.next=newVal
            self.last=newVal
        self.length+=1
        return self
    def dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length ==1:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
            temp.next=None
        self.length -=1
        return temp.value
    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next

myQueue=Queue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)
print(myQueue.dequeue())
print(myQueue.print_queue())
print(myQueue.dequeue())


