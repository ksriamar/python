lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
n = 4 
final = [lst[i * n:(i + 1) * n] for i in range((len(lst) + n - 1) // n )] 
print (final)