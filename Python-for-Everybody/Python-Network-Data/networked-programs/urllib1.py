"""
    Con urllib, es posible tratar una pagina web de forma parecida a un archivo.
    Se puede indicar simplemenete que pagina web se desea recuperar y urllib se encargara de manejar
    todos los detalles referentes al protocolo HTTP y a la cabecera
"""

import urllib.request as request

man_a = request.urlopen('http://data.pr4e.org/romeo.txt')

for linea in man_a:
    print(linea.decode().strip())