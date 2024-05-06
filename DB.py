import sqlite3

conn = sqlite3.connect("./Assignments/Library.db") 
cur = conn.cursor()

cur.execute('''SELECT * from person''')
print(cur.fetchall())


cur.close()
conn.close()