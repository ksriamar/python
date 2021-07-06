def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
newList = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    newList.append(ele) 
print(newList)
print(swapList(newList))