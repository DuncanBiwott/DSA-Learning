#Learning Lists
#Stores Different data types
mylist=[1,2,3,"Hello","World","Python"]
print(type(mylist))
print(len(mylist))
print(mylist[3])
print(mylist[-1])
print(mylist[1:4])
print(mylist[3:-1])
#Modify Item
mylist[0]="First"
print(mylist)
sublist=mylist[2:4]
print(sublist)
#Append to a List
mylist.extend(sublist)
mylist.append("Welcome")
mylist.insert(0,"Initial")
mylist.pop(0)
del mylist[2:4]
del mylist[-1]
print(mylist)
for item in mylist:
    print(item,end='_')


lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print ("lst[{}]: ".format(i), lst[i])
lists=[x*2 for x in lst if x%2==0]
print(lists)
list2=mylist.copy()
print(id(mylist))
print(id(list2))
print(list2)

#Joining a list using list Comprehension
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L4=L1+L2
print(L4)
L3 = [y for x in [L1, L2] for y in x]
print ("Joined list:", L3)
L4.clear()
print(L1.count(20))
L1.remove(10)
L1.reverse()
print(L1)
print(L4)


print(lst.sort())