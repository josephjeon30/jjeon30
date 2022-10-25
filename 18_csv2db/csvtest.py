import csv

with open('courses.csv') as courses_data:
    reader = csv.DictReader(courses_data)
    print("Data:")
    for row in reader:
        print(row)

with open('students.csv') as students_data:
    reader = csv.DictReader(students_data)
    print("Data:")
    for row in reader:
        print(row)      

print(csv.DictReader(courses_data))