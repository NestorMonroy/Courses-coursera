import sqlite3

conn = sqlite3.connect('week5.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('''CREATE TABLE Ages( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                                    name VARCHAR(128), 
                                    age INTEGER) ''')

cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Winnifred', 16));
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Kaysey', 23));
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Meagan', 25));
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Joan', 18));

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X');
for row in cur:
    print(row)
    
cur.close()
