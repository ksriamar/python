
fav_lang = {'amar': ['python', 'c'], 'nitesh': ['R','python'], 'abhi': ['ruby', 'go'], 'mohit': ['python'],}
for name, languages in fav_lang.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())