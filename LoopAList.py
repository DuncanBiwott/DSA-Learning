num=[1,1,1,2,2,2,3,4,5,6,6]
numSquare=[]
for i in num:
    numSquare.append(i*i)

print(numSquare)
squareVal=[x*x for x in num]
print(squareVal)

numsum=0
for i in num:
    numsum+=i
print(numsum)

greater=0
for i in num:
    greater=max(greater,i)
print(greater)