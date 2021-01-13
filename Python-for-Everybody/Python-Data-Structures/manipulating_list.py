#Concatenating List Using +

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#List Can be Sliced Using
#Remember: Just like in string, the second number is "up to but not including"

t = [9, 41, 12, 3, 74, 12]
t[1:3]
t[:4]

#Building a list from scratch
#add element with append
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

stuff.append('cookie')
print(stuff)

#lists are in oder

friends = ['Josep', 'Glenn', "Sally"]
friends.sort()
print(friends)
print(friends[1])

