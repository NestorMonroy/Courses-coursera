import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # http://py4e-data.dr-chuck.net/known_by_Fikret.html
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Maisha.html'

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
