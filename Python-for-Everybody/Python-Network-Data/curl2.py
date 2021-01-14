"""
    En este ejemplo, leemos solamente 100,000 caracteres a la vez, y después los escribimos al archivo portada2.jpg
    antes de obtener los siguientes 100,000 caracteres de datos desde la web
    
"""
import urllib.request 

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
man_a=open('portada2.jpg','wb')
tamano = 0

while True:
    info = img.read(100000)
    if len(info) < 1 : break
    tamano = tamano + len(info)
    man_a.write(info)

print(tamano, 'Caracteres copiados')

man_a.close()