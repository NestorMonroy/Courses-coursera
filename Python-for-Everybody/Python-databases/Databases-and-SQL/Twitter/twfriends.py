"""
    1. Crear tablas con claves primarias y restricciones.
    2. Cuando tenemos una clave lógica para una persona (es decir, un nombre de cuenta) 
        y necesitamos el valor del id de esa persona, dependiendo de si esa persona ya 
        está en la tabla People o no, tendremos que: 
            (1) buscar la persona en la tabla People y recuperar el valor de id para esa 
                persona, o
            (2) añadir la persona a la tabla People y obtener el valor del id para la 
                fila recién añadida.
    3. Insertar la fila que indica la relación de “seguimiento"

    
"""

import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS People
            (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''') #Estamos indicando que la columna name debe ser UNIQUE
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
            (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''') #Estamos indicando que la combinacion de los dos numeros debe der UNIQUE

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT id, name FROM People WHERE retrieved=0 LIMIT 1')
        try:
            (id, acct) = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        """
            Cuando pedimos al usuario una cuenta de TW, si la cuenta existe debemos de averiguar 
            el valor del id  (id = cur.fetchone()[0]), si la cuenta no exite en la tabla People debemos
            de inserta el valor (INSERT OR IGNORE INTO People) y obtener el valor del id de la ultima 
            fila insertada  (id = cur.lastrowid)

        """
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (acct, ))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('''INSERT OR IGNORE INTO People
                        (name, retrieved) VALUES (?, 0)''', (acct, )) #Se anade la clausula OR IGNORE para indicar que si este INSERT en particular causara una violacion de regla "el nombre debe ser unico", el sistema esta autorizado a ignorar el INSERT
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    print('Retrieving account', acct)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Failed to Retrieve', err)
        break

    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except:
        print('Unable to parse json')
        print(data)
        break

    # Debugging
    # print(json.dumps(js, indent=4))

    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
                        VALUES (?, 0)''', (friend, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid
            countnew = countnew + 1
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
                    VALUES (?, ?)''', (id, friend_id)) #Se asegura que no anademos exactamente la misma relacion dos veces, se le indica a la base de datos que ignore cualquier intento de INSERT si viola la regla
    print('New accounts=', countnew, ' revisited=', countold)
    print('Remaining', headers['x-rate-limit-remaining'])
    conn.commit()
cur.close()


