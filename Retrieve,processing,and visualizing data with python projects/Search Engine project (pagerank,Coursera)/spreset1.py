import sqlite3
connsqlite3.connect('spider.sqlite')
cur.commit()

cur.close()

print("a6ll pages set a rank of 1.0")
