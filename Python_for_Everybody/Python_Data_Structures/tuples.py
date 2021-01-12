#Tuples are like list
"""
    Tuples aremore Efficient
    Since Python does not have to build tuples structures to be
    modifiable, they are simpler and more efficient in items of
    memory use and perfomand than list

    So in our program when we are "temporary variables"
    we perfer tuples over list

"""
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y)

print(max(y))

for i in y:
    print(i)

#Tuples are "immutable"

z= (5, 4, 3)
z[1] = 0 #Error

#Tuples and Assignment

"""
    We can also put a tuple on the left-hand side of an assignment statement.
    We can even ommit the parentheses

"""

(x,y) = (4, 'freed')
print(y)

(a, b) = (99, 98)
print(a)

#Tuples and Dictonaries

d = dict()
d['csev'] = 2
d['cwen'] = 50

for k,v in d.items():
    print(k, v)

tups = d.items()
print(tups)

#Tuples are Comparable

(0, 1, 3) < (5, 1, 2)

#Sorting list of tuples

"""
    We can take advantage of the aviliti to sort a list of tuples to get 
    sorted version of a dictionary

    First we sort the dictionary by the key using the items() method 
    and sorted() function
"""
d = {'a':10, 'b':1, 'c': 22}
d.items()

dict_items = d.items()
print(dict_items)

sorted(d.items())


d = {'a':10, 'b':1, 'c': 22}

t = sorted(d.items())

print(t)

for k,v in d.items():
    print(k, v)

#Sort by values instead of key
c = {'a':10, 'b':1, 'c': 22}
tmp = list()

for k, v in c.items():
    tmp.append((v, k))

print(tmp)

tmp = sorted(tmp, reverse=True )
print(tmp)


#Even Shorter Version

c = {'a':10, 'b':1, 'c': 22}
print(sorted([ (v, k) for k, v in c.items() ]))

