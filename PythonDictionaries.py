#Uses Key Value Pairs,Tuples,Number,String as Keys Cannot Use List
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print(capitals|numbers|marks)#Concatenation of Dictionaries
capitals["Maharashtra"]="Kenya"
capitals.update({"Maharashtra":"Uganda"})


capitals["Kerala"]="Thiruvananthapuram"
print(capitals["Maharashtra"])
print(capitals.get("Maha"))

print(capitals.keys())
print(capitals.values())
print(capitals|numbers)

l1={"4":"Zour","1":"One","2":"Two"}
print("**************************************")
l5=sorted(l1.values())
print(l5)
print(l1.items())
l2={"3":"Three","4":"Four"}
l3=l1.copy()
#Concatenation of Dictionaries
print(l1|l2)
print(l1.get("1"))
print(l3)
del l1["1"]
print(l1)
print(l1.pop("2"))
l1.clear()
print(l1)
print(l1)
l2.popitem()
print(l2)

import sys
print("**************************************")
sorted_keys=sorted(capitals.keys())
print(capitals.__sizeof__())
print(sys.getsizeof(capitals))
print("**************************************")

my_dict = {'one':100,'Jack':200, 'age': 26}
print(sum(my_dict.values()))
print(my_dict.__sizeof__())
print(sys.getsizeof(my_dict))

print("**************************************")
#Remove Duplicates in Words

from collections import Counter

def remov_duplicates(input):

	# split input string separated by space
	input = input.split(" ")

	# now create dictionary using counter method
	# which will have strings as key and their
	# frequencies as value
	UniqW = Counter(input)

	# joins two adjacent elements in iterable way
	s = " ".join(UniqW.keys())
	print (s)
input = 'Python is great and Java is also great'
