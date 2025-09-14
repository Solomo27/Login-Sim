import sqlite3

conn = sqlite3.connect('LoginData.db')
cursor = conn.cursor()

cmd1 = """CREATE TABLE IF NOT EXISTS Users(
userID INTEGER PRIMARY KEY, 
first_name TEXT,
last_name TEXT,
email TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
)"""

cursor.execute(cmd1)

cmd2 = """INSERT INTO Users(first_name, last_name, email, password)
VALUES (
'test',
'tester',
'tester@gmail.com',
'tester'
)"""

cursor.execute(cmd2)
conn.commit()
row = cursor.execute("select * from Users").fetchall()
print(row)
conn.close()