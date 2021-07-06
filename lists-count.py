'''
def countAB(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
lst = [21, 34, 55, 6, 55, 55, 55, 7, 0]
x = 55
print('{} has occurred {} times'.format(x, countAB(lst, x)))
'''
def countAB(lst, x):
    return lst.count(x)  #using count method
lst = [21, 34, 55, 6, 55, 55, 55, 7, 0]
x = 55
print('{} has occurred {} times'.format(x, countAB(lst, x))) 