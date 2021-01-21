import sqlite3

# conn = sqlite3.connect('spider.sqlite')
# cur = conn.cursor()
# cur.execute('SELECT * FROM Twitter')
# count = 0
# for row in cur:
#     print(row)
#     count = count + 1
# print(count, 'rows.')
# cur.close()


conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()
#cur.execute('SELECT * FROM People')
cur.execute('SELECT * FROM Follows')


count = 0
for row in cur:
    print(row)
    count = count + 1
print(count, 'rows.')
cur.close()

