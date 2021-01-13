"""
    List are mutable

    String are "inmutable" - we cannont change the contents of a string-
    we must make a new string to make any change

    List are "mutable" we can change an element of a list using the index 
    operator

"""

fruit = ['Banana']
fruit[0]= 'b' # error

x = fruit.lower()
print(x)

lotto = [2, 15, 26, 41, 63 ]
print(lotto)

lotto[2]= 28
print(lotto)

# How long is a list

greet = 'Hello Boke'
print(len(greet))

x = [1, 4, 'joe', 99]
print(len(x))

# using the range function 
"""
    The range function returns a list of numbers that range from 
    zero to one less than the parameter value
    
    We can construct an index loop using for and integer iterator
"""


print(range(4))

friends = ['joel', 'david', 'jon']
print(len(friends))

print(range(len(friends)))

# A tale of two loops
friends = ['joel', 'david', 'jon']

for friend in friends:
    print('Happy new year: ', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year: ', friend)

print(len(friends))

print(range(len(friends)))