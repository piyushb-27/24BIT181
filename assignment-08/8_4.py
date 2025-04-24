'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Split names into sets A and B
s = {"Amit", "Anil", "Bhavesh", "Bhavin", "Ajay", "Bharat"}
a_set = {name for name in s if name.startswith("A")}
b_set = {name for name in s if name.startswith("B")}
print(a_set)
print(b_set)
