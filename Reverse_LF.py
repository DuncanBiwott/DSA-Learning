my_list=[1,2,3,4,5,6,7,8,9,10]
temp=my_list[0]
my_list[0]=my_list[-1]
my_list[-1]=temp
print(my_list)

values=[[x,y] for x in my_list for y in my_list if x+y==19]
print(values)
def sum_two_nums(my_sum):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if my_list[i]+my_list[j]==my_sum:
                # print(my_list[i],my_list[j])
                return True


#With one Loop to keep track of the visited elements
def sum_nums(my_sum):
    visited=[]
    for i in range(len(my_list)):
        if my_sum-my_list[i] in visited:
            print(my_list[i],my_sum-my_list[i])
            return True
        else:
            visited.append(my_list[i])
    return False

print(sum_nums(21))