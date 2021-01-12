# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)


"""
    The get method for dictionaries
    
    The pattern of checking to see if a key is alredy in and assuming
    a defaul value if the key is not there is so common that there is
    a method called get() that does this for us

    We can use get() and provide a default value of zero when the key
    is not yet in the dictonary - and then just add one

"""

#Default value if key does not exist(and no Traceback)
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1

print(counts)