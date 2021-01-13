abc = 'With three words'
stuff = abc.split()
#    Split break a string into parts and produces a list of string

print(stuff)
print(len(stuff))

print(stuff[0])

print(stuff)

for w in stuff:
    print(w)

#  When you do not specify a delimiter, multiple spaces are treated like one delimiter

line = 'A lot                  of spaces'
etc = line.split()
print(etc)

#   You can specify what delimiter character to use in the splitting

line = ['first;second;third']

thing = line.split(';')
print(thing)
print(len(thing))



