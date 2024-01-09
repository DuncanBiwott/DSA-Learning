def reverse(nums):
    last_index=len(nums)-1
    start_index=0
    while start_index<last_index:
        nums[start_index],nums[last_index]=nums[last_index],nums[start_index]
        start_index+=1
        last_index-=1
    print(nums)
nums=[1,2,3,4,5,6,7,8,9]
reverse(nums)

#Reversing an Interger
def reverse_integer(num):
    reverse=0
    while num>0:
        remainder=num%10
        reverse=reverse*10+remainder
        num=num//10
    print(reverse)
reverse_integer(12345)