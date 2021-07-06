def Cloning(lst1):
    lst_copy =[]
    for item in lst1: lst_copy.append(item)
    return lst_copy

lst1 = [1, 2, 3, 4, 5]
lst2 = Cloning(lst1)
print("Before Cloning:", lst1)
print("After Cloning:", lst2)