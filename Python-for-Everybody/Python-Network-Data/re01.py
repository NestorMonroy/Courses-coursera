import re
man = open('mbox-short.txt')
#count = 0
# Búsqueda de líneas que contengan 'From'
for line in man:
    
    line = line.strip()

    if re.search('From:', line):
        #count += 1
        print(line)
        
#print(count)

"""
    You can use re.search() to see if a string matches a regular expression, similar to using method find()

    You can use re.findall() to extract portions of a string that match your regular expresion,
    similar to a combination of find() and slicing

"""