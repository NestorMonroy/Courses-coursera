from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #http://py4e-data.dr-chuck.net/comments_1129446.html
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
ltags = []
for tag in tags:
    
    ltags.append(tag.contents[0])

final = [int(ltags) for ltags in ltags]

print(sum(final))