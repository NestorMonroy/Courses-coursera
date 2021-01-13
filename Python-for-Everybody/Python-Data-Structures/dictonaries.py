purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)

print(purse['candy'])
#dictonary are mutables

purse['candy'] = purse['candy'] + 2
print(purse)

#dictonary literals use curly braces and have a list of key: value pairs
#you can make a empty dictonary using empty curly braces

jjj = {'chuck': 1, 'fred':42, 'jan':100}

print(jjj)
ooo = {}
print(ooo)

#Definite loops and dictionaries

counts = {'chuck': 1, 'fred':42, 'jan':100}
for key in counts:
    print(key, counts[key])


#Retrieving list of keys and values
jjj = {'chuck': 1, 'fred':42, 'jan':100}

print(list(jjj)) #list of keys

print(jjj.keys()) #list of keys

print(jjj.values()) #list of values

print(jjj.items()) # return tuple


#Two iteration variables
#Each iteration, the first variable is the key and the second is value

jjj = {'chuck': 1, 'fred':42, 'jan':100}
for aaa, bbb in jjj.items():
    print(aaa, bbb)



