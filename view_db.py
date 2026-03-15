import sqlite3
conn = sqlite3.connect("habits.db")
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(habits)")
print(cursor.fetchall())