"""
    (*, +)
    Estos caracteres especiales indican queen lugar de coincidir 
    con un solo carácter en la cadena de búsqueda, 
    coinciden con cero  o más caracteres (en el caso del asterisco) o 
    con uno o más caracteres (en el caso del signo de suma)

"""

import re
man = open('mbox-short.txt')

# Búsqueda de líneas que comienzan con From y tienen una arroba

count = 0
for line in man:
    line = line.strip()
    if re.search('^From:.+@', line):
        count +=1
        print(line)

print(count)


"""
    La cadenaˆFrom:.+@retornará coincidencias con líneas que empiecen con 
    “From:”,seguidas de uno o más caracteres (.+), seguidas de un carácter @. 
    Por lo tanto, lasiguiente línea coincidirá

    From: stephen.marquard@uct.ac.za

"""