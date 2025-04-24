'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Read CSV, convert to dict and display with total
d = {}
with open("students.csv", "r") as f:
    lines = f.readlines()[1:]
    for line in lines:
        parts = line.strip().split(",")
        roll = parts[0]
        name = parts[1]
        marks = list(map(int, parts[2:]))
        total = sum(marks)
        d[roll] = {"name": name, "marks": marks, "total": total}
print(d)
