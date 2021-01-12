"""
    Write a program to read through the mbox-short.txt and figure out 
    who has sent the greatest number of mail messages. The program looks 
    for 'From ' lines and takes the second word of those lines as the person 
    who sent the mail. The program creates a Python dictionary that maps 
    the sender's mail address to a count of the number of times they appear 
    in the file. After the dictionary is produced, the program reads through 
    the dictionary using a maximum loop to find the most prolific committer.

"""
fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
handle = open(fname)

elist = []
edict = {}

for line in handle:
    line = line.strip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    elist.append(email)

#print(elist)

for email in elist:
    edict[email] = edict.get(email, 0) + 1

#print(edict)

bigkey = None
bigvalue = None

for key, value in edict.items():
    if bigkey is None or value > bigvalue:
        bigkey = key
        bigvalue = value

print(bigkey, bigvalue)
