import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor() #es como un manejador de archivos, esta llamada es muy similar conceptualmente a la llamada open()
#con .execute se pueden empezar a ejecutar comandos sobre el contenido
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER) ')

conn.close()