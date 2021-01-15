from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Ignorar errores de certificado SSL
# Para ejecutar este programa descarga BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode =  ssl.CERT_NONE

url = input('Introduzca - ') # https://docs.python.org / http://www.dr-chuck.com/page1.htm
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Recuperar todas las etiquetas de anclaje

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

