#Return list of Index which add to target


indexes=[]
adds_to_target = [1,2,3,4 ]
target = 7

def add_to_target(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                indexes.append([i,j])
    print(indexes)


array_List=[[i,j] for i in range(len(adds_to_target))  for j in range(i+1,len(adds_to_target)) if adds_to_target[i]+adds_to_target[j]==target and adds_to_target[len(adds_to_target)-1]!=target and adds_to_target[i]!=target and adds_to_target[j]!=target]
print(array_List)



#Permutation of a List of Numbers
def permute_val(nums):
    if len(nums)==0:
        return []
    if len(nums)==1:
        return [nums]
    result=[]
    for i in range(len(nums)):
        m=nums[i]
        remaining_list=nums[:i]+nums[i+1:]
        for p in permute_val(remaining_list):
            result.append([m]+p)
    print(result)

permute_val([1,2,3,4])