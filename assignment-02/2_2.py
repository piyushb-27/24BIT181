'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 2. Largest and smallest of three numbers
a = 10
b = 30
c = 20

if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c

if a < b and a < c:
    smallest = a
elif b < c:
    smallest = b
else:
    smallest = c

print("largest:", largest)
print("smallest:", smallest)
