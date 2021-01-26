import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER) ')

cur.execute('INSERT INTO Ages (name, age) values (? ,?)', ('Jema', 40));
cur.execute('INSERT INTO Ages (name, age) values (? ,?)', ('Ailsa', 14));
cur.execute('INSERT INTO Ages (name, age) values (? ,?)', ('Amaan', 19));
cur.execute('INSERT INTO Ages (name, age) values (? ,?)', ('Riven', 22));
cur.execute('INSERT INTO Ages (name, age) values (? ,?)', ('Alena', 22));
cur.execute('INSERT INTO Ages (name, age) values (? ,?)', ('Alighia', 40));
conn.commit()

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur:
    print(row)

conn.close()