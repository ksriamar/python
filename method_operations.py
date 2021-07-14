# dict_key
'''
adict = {'color': 'black', 'age': 21 , 'car': 'polo'} 
for k in adict.keys(): 
    print(k)
'''
adict= {'color': 'red', 'age': 42} 
print(adict.keys())
print(list(spam.keys()))
# dict_values
'''
adict = {'color': 'black', 'age': 21 , 'car': 'polo'} 
for v in adict.values():
    print(v)
'''

#dict_items
'''
adict = {'color': 'black', 'age': 21, 'car': 'polo'} 
for k, v in adict.items():
    print('Key: ' + k + ' Value: ' + str(v))
'''

# setdefault
adict = {'name': 'amar', 'age': 21}
print(adict.setdefault('color', 'blue'))