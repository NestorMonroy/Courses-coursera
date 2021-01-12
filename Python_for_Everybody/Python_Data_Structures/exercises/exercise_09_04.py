"""
    Write a program to read through the mbox-short.txt and figure out 
    who has sent the greatest number of mail messages. The program looks 
    for 'From ' lines and takes the second word of those lines as the person 
    who sent the mail. The program creates a Python dictionary that maps 
    the sender's mail address to a count of the number of times they appear 
    in the file. After the dictionary is produced, the program reads through 
    the dictionary using a maximum loop to find the most prolific committer.

"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dictsemail = dict()
lst = list()

for line in handle:
    if not line.startswith('From ') : continue
    line = line.split()
    email = line[1]
    lst.append(email)

#print(lst)

for word in lst:
    dictsemail[word] = dictsemail.get(word, 0) + 1

#print(dictsemail)


bigcount = None
bigword = None

for key, values in dictsemail.items():
    if bigcount is None or values > bigcount:
        bigword = key
        bigcount = values

print(bigword, bigcount)




