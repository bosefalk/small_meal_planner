import sqlite3, csv

conn = sqlite3.connect("meals.db")

c = conn.cursor()

c.execute('''CREATE TABLE meals (meal text, weight integer default1)''')
#c.execute("DROP TABLE meals")

conn.commit()

conn.close()