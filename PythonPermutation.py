from itertools import permutations


# [1,2,3,4]
def all_permutation(mylist):
    if mylist == 0:
        return mylist
    if mylist == 1:
        return mylist[0]
    result = []
    for i in range(len(mylist)):
        m = list(mylist[i])
        remaining_list = mylist[:i] + mylist[i + 1:]
        for j in permutations(remaining_list):
            result.append(m.extend(j))
    print(result)


pList = [1, 2, 3, 4]
all_permutation(pList)
