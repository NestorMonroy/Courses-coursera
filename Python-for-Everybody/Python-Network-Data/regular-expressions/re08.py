import re

handle = open('mbox-short.txt')

"""
    ^X-.*: [0-9.]+ 
    Queremos lineas que empiecen con X-,
    seguido por 0 o mas caracteres (.*),
    seguido por un caracter de dos puntos (:) y luego un espacio ( )
    despues del espacio buscamos uno o mas caracteres que sean, o bien
    un digito (0-9) o bien un punto [0-9.]+


"""

# Búsqueda de líneas que comiencen con 'X' seguida de cualquier caracter que
# no sea espacio y ':' seguido de un espacio y cualquier número.
# El número incluye decimales

for line in handle:
    line = line.rstrip()
    if re.search(r'^X-.*: [0-9.]+', line):
    #if re.search(r'^X\S*: [0-9.]+', line):
        print(line)
    
