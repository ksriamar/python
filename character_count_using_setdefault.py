# preety printing
#  pprint.pprint( )
import pprint
message = 'I am 21 years of age'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)