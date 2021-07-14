Things = {'rope': 1, 'plough': 2, 'coin': 3, 'axe': 4, 'knife': 5}
def displayContainer(container):
    print("Container:")
    item_total = 0
    for k, v in container.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
displayContainer(Things)