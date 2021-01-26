import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Artist')
count = 0
print('Artist')

# for row in cur:
#     if count < 5 : print(row)
#     count +=1
# print(count, 'rows')

cur.execute('SELECT * FROM Album')
count = 0
print('Album')

# for row in cur:
#     if count < 5 : print(row)
#     count +=1
# print(count, 'rows')


cur.execute('SELECT * FROM Track')
count = 0
print('Track')

# for row in cur:
#     if count < 5 : print(row)
#     count +=1
# print(count, 'rows')


cur.execute(''' SELECT T.title, Al.title,  Ar.name  FROM 
                Artist Ar JOIN Album Al JOIN Track T
                ON Ar.id = Al.artist_id 
                AND Al.id = T.album_id
                Where Ar.id = 1

''' )
count = 0

for row in cur:
    if count < 20 : print(row)
    count += 1
print(count, 'rows')

cur.close()