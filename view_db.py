import sqlite3

conn = sqlite3.connect("habits.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM habits")

rows = cursor.fetchall()

print(rows)

for row in rows:
    print(row)

conn.close()