
"""
    Buscar líneas que empiecen conDetails:, 
    seguida de cualquier número de caracteres (.*), 
    seguida de rev=, y después de uno o más dígitos. 
    Queremos encontrar líneas que coincidan con toda la expresión pero 
    solo queremos extraer el número entero al final de la línea, por lo 
    que ponemos[0-9]+ entre paréntesis
"""

#Busqueda de lineas que comiencen con 'Details: rev=' 
#seguido de numeros y '.'
#Despues imprimir el numero si es mayor a cero

import re
handle = open('mbox-short.txt')

for line in handle:
    line = line.rstrip()
    x = re.findall(r'^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)
