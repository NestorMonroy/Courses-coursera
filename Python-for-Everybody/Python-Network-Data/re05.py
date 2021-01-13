"""
    Para extrar datos de una cadena de datos podemos usar findall()
    (\S) = secuencia de dos caracteres que coincide con un carácter distinto a un espacio en blanco
"""

import re
s = 'Una nota de csev@umich.edu a cwen@iupui.edu sobre una reunión  @ 2PM'

lst = re.findall(r'\S+@\S+', s)
print(lst)
