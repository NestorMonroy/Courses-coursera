import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM User')
count = 0
print('User')

for row in cur:
    if count < 5 : print(row)
    count +=1
print(count, 'rows. ')


cur.execute('SELECT * FROM Member')
count = 0
print('Member')

for row in cur:
    if count < 5 : print(row)
    count +=1
print(count, 'rows. ')


cur.execute('SELECT * FROM Course')
count = 0
print('Course')

for row in cur:
    if count < 5 : print(row)
    count +=1
print(count, 'rows. ')


sqlstr = ''' SELECT U.name, M.role, C.title FROM 
            User U JOIN Member M JOIN Course C
            ON U.id = M.user_id
            AND C.id = M.course_id
            ORDER BY C.title, M.role DESC, U.name
'''



for row in cur.execute(sqlstr):
    print(str(row[0]), row[1], row[2])
cur.close()