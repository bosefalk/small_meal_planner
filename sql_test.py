# Grab all rows from database

import sqlite3, random

conn = sqlite3.connect("meals.db")

c = conn.cursor()

#c.execute("SELECT * FROM meal_list")
c.execute("SELECT meal FROM meal_list")
meals = c.fetchall()

aa = list(meals[1:])

print(aa)


bb = aa[1][0]

print(bb)


conn.commit()

conn.close()