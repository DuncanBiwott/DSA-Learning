#set is a collection of distinct objects enclosed with {} it is Immutable
#not an ordered collection
# items in a set or not accessible by its positional index
s1 = {"Rohan", "Physics", 21, 69.75,1,2,3}
s2 = {1, 2, 3, 4, 5}
s3 = {"a", "b", "c", "d"}
s4 = {25.50, True, -55, 1+2j}
s1.add("Rohannn")
s1.update(s2)

list1=["ok","Yes","Very True",1]
print(s1.union(list1))

print("Before Removing item")
s1.remove(1)
s1.remove(2)
print("After Removing item",s1)
print(s1)

for item in s1:
    print(item)

print(21 in s1)
print (s1)
print (s2)
print (s3)
print (s4)
s1.difference_update(s2)
print(s1.difference(s2))
print(s1)