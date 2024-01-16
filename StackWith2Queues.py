#Implementing 3 stacks with 2 queues
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue1:
    def __init__(self,value=None):
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
        return temp.data
    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.data)
            temp=temp.next
class Queue2:
    def __init__(self,value=None):
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
        return temp.data

def push(q1,q2,element):
    #Q1 is the source queue
    if q1.length==0:
        q1.enqueue(element)
    else:

        while q1.length>0:
            q2.enqueue(q1.dequeue())
        q2.enqueue(element)
        while q2.length>0:
            q1.enqueue(q2.dequeue())

def pop(q1):
    if q1.length==0:
        print("Stack is empty")
        return None

    else:
       q1.dequeue()
    return q1.print_queue()




q1=Queue1(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
q1.enqueue(7)
q1.enqueue(8)

q2=Queue2()

push(q1,q2,10)
print("**************************************")
q1.print_queue()
print("**************************************")
pop(q1)

hello= [0,1,3]*3
print(hello)