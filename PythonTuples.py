
#A Python tuple is a sequence of comma separated items, enclosed in parentheses (). The items in a Python tuple need not be of same data type.
#Differs with List by being Immutable cannot be modified
tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1+2j)
list1=list(tup1)

list1[0]="Duncan"
tup=tuple(list1)

print(tup)
print(tup.count("Duncan"))
print(tup.index(0))
print(type(tup))