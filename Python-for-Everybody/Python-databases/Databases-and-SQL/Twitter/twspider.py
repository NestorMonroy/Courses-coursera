from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite') #Nuestra base de datos se almacena en spider.sqlite
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTEGER)''') 
            
            # Cada fila de la tabla Twitter contiene una columna para 
            # el nombre de la cuenta,  
            # otra para indicar si hemos recuperado los amigos de la cuenta y 
            # otra para guardar cuantas veces se ha visto esa cuenta añadida en la lista de amigos de las demas

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Si el usuario introduce una cuenta de TW, recuperamos la lista de amigos de ese usuario junto con sus estados y añadimos cada amigo a la base de datos (si no esta en ella)
    # Si el amigo ya estaba en la lista, enumeramos en 1 el campo friends en la fila correspondiente de la base de datos
    # Si el usuario presiona intro, buscamos en la base de datos la siguiete cuenta de TW que no haya sido aun recuperada, recuperamos los amigos de esa cuenta junto con sus estados y los anadidos a la base de datos o los actualizamos, e incrementamos el contador del campo friends

    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        # Como hemos pulsado intro (es decir, no hemos especificado otra cuenta de Twitter),
        # se ha ejecutado el código siguiente:
        # Usamos la sentencia de SQLSELECT para obtener el nombre del primer usuario(LIMIT 1) 
        # que aún tiene su valor de “hemos recuperado ya este usuario” a cero.
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            # También usamos el patrón fetchone()[0] en un bloque try/except para extraer el 
            # “nombre a mostrar” (screen_name) de los datos recuperados, o bien mostrar un 
            # mensaje de error y volver al principio.

            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue
    
    # Si hemos obtenido con éxito el nombre de una cuenta que aún no había sido procesada, 
    # recuperamos sus datos de este modo:

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    # print json.dumps(js, indent=4)

    # Una vez recuperados correctamente los datos, usamos la sentencia UPDATE para poner la 
    # columna recuperado a 1, lo que indica que hemos terminado la extracción de amigos de 
    # esa cuenta. Esto impide que recuperemos los mismos datos una y otra vez, y nos permite 
    # ir avanzando a través de la red de amigos de Twitter

    
    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))

    # Una vez recuperado la lista de amigos y sus estados, nos movemos a traves de los elementos 
    # user del JSON devuelvo y recuperamos el screen_name(nombrea mostrar) de cada usuario. 

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        # Usamos esta sentencia para comprobar si ya tenemos almacenado ese nombre en la base de datos, si es asi
        # recuperamos su contador de amigos (friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
        # Una vez que el cursor ejecuta la sentencia SELECT, tenemos que recuperar las filas.
        # Podríamos hacerlo con una sentencia for, pero dado que sólo estamos recuperando una 
        # única fila (LIMIT 1), podemos también usar el método fetchone() para ex-traer la 
        # primera (y única) fila que da como resultado la operación SELECT
            count = cur.fetchone()[0] #fetchone() devulve la fila como una tupla (incluso si solo contiene un campo), tomamos el primer valor de la tupla mediante [0] para almacenarla en la variable count el valor del contador de amigos actual
            
            # Si esta operación tiene éxito, usamos la sentencia UPDATE de SQL con una clausula WHERE 
            # para añadir 1 a la columa friends de aquella fila que coincida con la cuenta del friend. 
            # hay dos marcadores de posición (es decir, signos de interrogación) en el SQL, y que el 
            # segundo parámetro de execute() es una tupla de dos elementos que contiene los valores 
            # que serán sustituidos por esas interrogaciones dentro de la sentencia SQL

            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend))
            countold = countold + 1
        except:
            # Si el código en el bloque try falla, se deberá probablemente a que ningún registro coincide 
            # con lo especificado en la clausula WHERE name = ? de la setencia SELECT. Así que en el bloque
            # except, usamos la sentencia de SQLI NSERT para añadir el nombre a mostrar (screen_name) del 
            # amigo (friend) a la tabla, junto con una indicación de que no lo hemos recuperado aún, y fijamos su 
            # contador de amigos a uno
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()

cur.close()
