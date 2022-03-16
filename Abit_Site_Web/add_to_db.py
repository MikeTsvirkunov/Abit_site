import sqlite3

con = sqlite3.connect('fuckults.db')
cur = con.cursor()

cur.execute("insert into fuck values (?, ?, ?, ?, ?)", (int(input()), input(), input(), input(), int(input())))
con.commit()
con.close()