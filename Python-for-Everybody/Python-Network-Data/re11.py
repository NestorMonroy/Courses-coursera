"""
    Ejercicio para obtener la hora del mail
        From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

    ^From .* ([0-9][0-9]):

    buscar líneas que empiecen con From(nótese el espacio), 
    seguido de cualquier número de caracteres(.*), 
    seguidos de un espacio en blanco, 
    seguido de dos dígitos[0-9][0-9], 
    seguidosde un carácter “:”. 

    para extrar la hora se agregan ()

"""

# Búsqueda de líneas que comienzan con From y un caracter seguido
# de un número de dos dígitos entre 00 y 99 seguido de ':'
# Después imprimir el número si este es mayor a cero
import re
handle =open('mbox-short.txt')

for line in handle:
    line = line.rstrip()
    x = re.findall(r'^From .* ([0-9][0-9]):', line)
    if len(x) > 0 : print(x)