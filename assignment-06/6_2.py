'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Split a list of student data into three separate lists

students = [
    (101, "Ravi", 18),
    (102, "Asha", 19),
    (103, "Kunal", 18),
    (104, "Seema", 20)
]

roll_nos = []
names = []
ages = []

for student in students:
    roll_nos.append(student[0])
    names.append(student[1])
    ages.append(student[2])

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)
