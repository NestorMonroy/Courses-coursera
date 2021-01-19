# Para ejecutar este programa descarga BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Ignorar los erroes de certificado

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduza: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parse')

tags = soup('a')

for tag in tags:
    print(tag.get('href', None))


