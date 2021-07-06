'''
def Reverse(lst):
    return [ele for ele in reversed(lst)]  # Using list comprehension
lst = [1, 2, 3, 4, 5]
print(Reverse(lst))
'''
def Reverse(lst):
    lst.reverse()  #Using reverse function
    return lst
lst = [1, 2, 3, 4, 5]
print(Reverse(lst))   
