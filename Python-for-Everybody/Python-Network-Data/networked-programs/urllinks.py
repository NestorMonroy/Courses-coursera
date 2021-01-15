import urllib.request
from bs4 import BeautifulSoup
import ssl

#Ignorar errores de certificado SSL
# Para ejecutar este programa descarga BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode =  ssl.CERT_NONE

url = input('Introduzca - ') # https://docs.python.org
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Recuperar todas las etiquetas de anclaje

etiquetas = soup('a')
for etiqueta in etiquetas:
    print(etiqueta.get('href', None))

