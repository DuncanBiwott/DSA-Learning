#Uses Key Value Pairs,Tuples,Number,String as Keys Cannot Use List
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print(capitals|numbers|marks)
capitals["Maharashtra"]="Kenya"
capitals.update({"Maharashtra":"Uganda"})


capitals["Kerala"]="Thiruvananthapuram"
print(capitals["Maharashtra"])
print(capitals.get("Maha"))

print(capitals.keys())
print(capitals.values())
print(capitals|numbers)

l1={"1":"One","2":"Two"}
l5=sorted(l1.keys())
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

for i,j in l3.items():
    print(i,j)