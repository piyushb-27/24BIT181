'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Create empty set, add 5 names, modify 1, delete 2
names = set()
names.add("Ravi")
names.add("Amit")
names.add("Rohit")
names.add("Kiran")
names.add("Priya")

names.remove("Ravi")
names.add("Ravindra")

names.discard("Kiran")
names.discard("Amit")

print(names)
