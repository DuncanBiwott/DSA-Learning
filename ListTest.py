
# Find Indexes of all values that adds to a target in a list it can be 2 and more values

#Find values to target which sum to target
my_list=[1,2,3,4,5,6,7,8,9,10]
target=35
sum_index=[[my_list.index(x),my_list.index(y)] for x in my_list for y in my_list if x+y==target]
print(sum_index)

#Finding index of x numbers in list that add up to target

# all Combination to target in a list



def find_val(num, target, values):
    if num == 1 or values == []:
        return [target] if target in values else []
    x, subvalues = values[0], values[1:]
    if subfound := find_val(num - 1, target - x, subvalues):
        return [x] + subfound
    else:
        return find_val(num, target, subvalues)

def find_ind(num,target, values, offset=0):
    if num == 1 or values == []:
        return [offset + values.index(target)] if target in values else []
    x, subvalues = values[0], values[1:]
    if subfound := find_ind(num - 1, target - x, subvalues, offset + 1):
        return [offset] + subfound
    else:
        return find_ind(num, target, subvalues, offset + 1)

values = [100, 150, 140, 100, 120, 270, 500, -100, 120, 150, 160]
target = 34
my_list=[1,2,3,4,5,6,7,8,9,10]

print(find_val(4, target, my_list))
print(find_ind(4, target, my_list))

