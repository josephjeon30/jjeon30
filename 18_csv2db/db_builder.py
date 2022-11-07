#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
#open our csv files

courses_data = open('courses.csv') #puts all the csv data from courses.csv into a string
courses_reader = csv.DictReader(courses_data) #turns that string into a list of dictionaries with each dict representing each row.

students_data = open('students.csv')
students_reader = csv.DictReader(students_data)     

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);") #creates a courses table with 3 columns: code, mark, id
c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER);") #creates a students table with 3 columns: name, age, id

for row in courses_reader: #for each dictionary in the list of dictionaries
    c.execute("INSERT INTO courses VALUES(\"" + row.get('code') + "\", " + row.get('mark') + ", " + row.get('id') + ")") #insert into the courses table each value of the dict keys

for row in students_reader:
    c.execute("INSERT INTO students VALUES(\"" + row.get('name') + "\", " + row.get('age') + ", " + row.get('id') + ")") #insert into the students table each value of the dict keys

#==========================================================

db.commit() #save changes
db.close()  #close database


