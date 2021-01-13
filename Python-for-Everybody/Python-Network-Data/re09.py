""" 
    Los paréntesis son otros caracteres especiales en las expresiones regulares. 
    Al agregar paréntesis a una expresión regular, son ignorados a la hora de 
    hacer coincidirla cadena. 
    
    Pero cuando se usa findall(), los paréntesis indican que, aunque se quiere 
    que toda la expresión coincida, solo interesa extraer una parte de la subca-dena 
    que coincida con la expresión regular.


"""

import re

handle = open('mbox-short.txt')
#Busqueda de lineas que comiencen con 'X' seguida de cualquier caracter que
#no sea espacio en blanco y ':' seguido de un espacio en
#El numero puede incluir decimales
#Despues imprimir el numero si es mayor a cero

for line in handle:
    line = line.rstrip()
    x = re.findall(r'^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)