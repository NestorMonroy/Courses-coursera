import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) values (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) values (?, ?)', ('My Way', 15))

conn.commit()

print('Tracks')
cur.execute('SELECT title, plays FROM Tracks')
#Despues de que ejecutamos la sentencia SELECT el cursor se convierte en algo con lo que podemos iterar
for row in cur:
    print(row)
cur.execute('UPDATE Tracks SET plays = 16 WHERE title ="My Way"' )
conn.commit()
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
cur.close()

