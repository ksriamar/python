students = {'amar': {'apples': 5, 'bananas': 12}, 'nitesh': {'Sandwiches': 3, 'apples': 2}, 'abhi': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(students, 'apples')))
print(' - Cups           ' + str(totalBrought(students, 'cups')))
print(' - Cakes          ' + str(totalBrought(students, 'cakes')))
print(' - Sandwiches     ' + str(totalBrought(students, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(students, 'apple pies')))

 