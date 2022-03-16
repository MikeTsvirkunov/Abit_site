import sqlite3

con = sqlite3.connect('fuckults.db')
cur = con.cursor()

for row in cur.execute('SELECT * FROM fuck ORDER BY size DESC'):
    print(row)
con.close()