import sqlite3
import csv

db = sqlite3.connect("foo")

c = db.cursor()

c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")

db.commit()
db.close()
