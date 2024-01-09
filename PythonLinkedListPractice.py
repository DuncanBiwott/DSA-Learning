'''

A LinkedList is a linear data structure,
in which the elements are not stored at contiguous memory locations.
The elements in a linked list are linked using pointers.
 SAMPLE LINKED LIST UNDER THE HOOD
  Head= {
  head: {
    value: 6
    next: {
      value: 10
      next: {
        value: 12
        next: {
          value: 3  ----Tail
          next: null
        }
      }
    }
  }
}

'''
'''
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


Operations on a Linked List
def prepend(self,value):
    new_node=Node(value)
    new_node.next=self.head
    self.head=new_node
def append(self,value):
    new_node=Node(value)
    if self.head is None:
        self.head=new_node
        return
    last_node=self.head
    while last_node.next:
        last_node=last_node.next
    last_node.next=new_node
    
def insert_after_node(self,prev_node,value):
    if not prev_node:
        print("Previous Node is not in the List")
        return
    new_node=Node(value)
    new_node.next=prev_node.next
    prev_node.next=new_node
'''
head={
    "value":6,
    "next":{
        "value":10,
        "next":{
            "value":12,
            "next":{
                "value":3,
                "next":None
            }
        }
    }
}
print(head["next"]["next"]["next"]["value"])

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length+=1
        return self
myNode=LinkedList(10)
myNode.print_list()
myNode.append(12)

