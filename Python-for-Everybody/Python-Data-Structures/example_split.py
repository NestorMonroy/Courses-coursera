"""
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
"""

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.strip()
#     if not line.startswith('From ') : continue
#     words = line.split()
#     print(words)
#     #print(words[2])


#The double split pattern

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])

    #print(words[2])

