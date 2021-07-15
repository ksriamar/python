'''
fav_lang = {'amar': 'python', 'nitesh': 'R', 'abhi': 'ruby', 'mohit': 'python',}
for name in fav_lang.keys():
    print(name.title())
'''

fav_lang = {'amar': 'python', 'nitesh': 'R', 'abhi': 'ruby', 'mohit': 'python',}
friends = ['abhi', 'nitesh']
for name in fav_lang.keys():
    print(name.title())
if name in friends:
    print(" Hi " + name.title() + ", I see your favorite language is " + fav_lang[name].title() + "!")