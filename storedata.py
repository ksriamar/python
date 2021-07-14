cars = {'amar': 'Apr 1', 'nitesh': 'Dec 12', 'abhi': 'Mar 4'}
while True:
    print('Enter a name:')
    name = input()
    if name == '':
       break
    if name in cars:
        print(cars[name] + ' is the date for servics ' + name + 'car')
    else:
        print('I do not have car service info for ' + name)
        print('What is their date for service ?')
        date = input()
        cars[name] = date
        print('date of service database updated.')