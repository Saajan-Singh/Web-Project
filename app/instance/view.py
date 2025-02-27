import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables in DB:", cursor.fetchall())

cursor.execute("SELECT * FROM user")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()