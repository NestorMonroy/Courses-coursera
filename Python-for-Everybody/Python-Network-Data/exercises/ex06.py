from urllib.request import urlopen
from urllib.parse import urlencode
import json
import ssl

api_key = False

#Si tienes una clave API de Google Places, ingresala aqui
#api_key = 'AIzaSy___IDByT70'
#https://developers.google.com/maps/documentation/geocoding/intro
#https://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    parms = dict()
    parms['address'] = address
    if api_key is not False : parms['key'] = api_key
    url = serviceurl + urlencode(parms)

    print('Retrieving', url)
    uh = urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    #print(js)

    place_id =  js['results'][0]['place_id']
    print(place_id)