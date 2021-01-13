"""
    Escapado de caracteres espciales ($, ^)
    Podemos indicar que queremos encontrar la coincidencia con un carácter 
    an-teponiéndole una barra invertida. 

    Nota:dentro de los corchetes, los caracteres no se consideran “especiales”. 
    Por tanto, al escribir[0-9.], efectivamente significa dígitos o un punto. 
    Cuando no está entre corchetes, el punto es el carácter “comodín” que coincide 
    con cualquier carácter. Cuando estádentro de corchetes, un punto es un punto

"""

import re

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9]+', x)

print(y)
