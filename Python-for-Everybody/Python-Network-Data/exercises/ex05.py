from urllib.request import urlopen
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca - ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1129449.json'

uh = urlopen(url, context=ctx)
data = uh.read().decode()

info = json.loads(data)

#print(json.dumps(info, indent=4))


#print('comments:', len(info['comments']), "\n")

count = 0
sum = 0

for item in info['comments']:
    count = count+1
    number = int(item['count']) # Number of comments
    sum = sum + number
print('Total count:', count)
print ('Sum:', sum)