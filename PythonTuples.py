
#A Python tuple is a sequence of comma separated items, enclosed in parentheses (). The items in a Python tuple need not be of same data type.
#Differs with List by being Immutable cannot be modified
# items in a tuple can be accessed using positional index

tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (7, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1+2j)
list1=list(tup1)

list1[0]="Duncan"
tup=tuple(list1)

print(tup)
print(tup.count("Duncan"))
print(sum(tup2))
print(max(tup2))
print(min(tup2))
print(len(tup2))
print(tup2.index(5))
print(sorted(tup2))
print(enumerate(tup2))

for item in enumerate(tup2):
    print(list(item))
print(any(tup2))
print(all(tup2))