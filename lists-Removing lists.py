lst = [6, 8, 3, [], [], 243, []]
print("original list : " + str(lst))
result = [ele for ele in lst if ele != []]  #Using list comprehension
result1 =list(filter(None, lst))
print ("after empty list removal : " + str(result))
print ("after empty list removal through filter: " + str(result1))

