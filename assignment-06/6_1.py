'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Count number of boys and girls in the list
# Boys' names are stored as tuples

names = ["Anjali", "Priya", ("Rohan",), "Meena", ("Amit",), "Neha", ("Raj",), "Sonal"]

boys = 0
girls = 0

for ele in names:
    if isinstance(ele, tuple):
        boys += 1
    else:
        girls += 1

print("Number of boys:", boys)
print("Number of girls:", girls)
