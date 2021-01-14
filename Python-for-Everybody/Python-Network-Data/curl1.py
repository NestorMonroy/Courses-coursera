"""
    Este programa lee todos los datos que recibe de la red y los almacena en la variable img en la memoria principal de la computadora. 
    Después, abre el archivo portada.jpg y escribe los datos en el disco. El argumento wb en la función open() abre un archivo binario 
    en modo de escritura solamente. Este programa funcionará siempre y cuando el tamaño del archivo sea menor que el tamaño de la memoria
    de la computadora
    
"""

import urllib.request 

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
man_a=open('portada.jpg','wb')
man_a.write(img)
man_a.close()