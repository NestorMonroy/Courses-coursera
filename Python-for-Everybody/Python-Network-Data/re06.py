# Búsqueda de líneas que tengan una arroba entre caracteres

import re
handle = open('mbox-short.txt')

count = 0
for line in handle:
    line = line.strip()
    x = re.findall(r'\S+@\S+', line)
    if len(x) > 0:
        count +=1
        print(x)

print(count)