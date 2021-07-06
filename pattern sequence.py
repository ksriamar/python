
'''
# for i in range(4):                            # # # #
#     for j in range(4):                        # # # #
#         print("# ",end=')                     # # # #                                            
#     print()                                   # # # #
'''
'''
for i in range(4):                              # # # # 
    for j in range(4 - i):                      # # #
        print("# ",end='')                      # # 
    print()                                     #
'''
'''
lastNumber = 6           
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
'''
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
