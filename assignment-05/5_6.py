'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Convert list of Fahrenheit temps to Celsius
f = [32, 68, 86, 104, 122]
c = []
for temp in f:
    cel = (temp - 32) * 5 / 9
    c.append(cel)
print("Fahrenheit:", f)
print("Celsius:", c)
