import re
man = open('mbox-short.txt')

# Búsqueda de líneas que comiencen con 'F', seguidas de 2 caracteres, seguidos de m
count = 0
for line in man:
    line = line.strip()
    if re.search('^F..m', line):
        count +=1
        print(line)

print(count)
