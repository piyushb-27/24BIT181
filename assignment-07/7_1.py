'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Create 3 dictionaries and concatenate into a 4th
d1 = {1: 'A', 2: 'B'}
d2 = {3: 'C', 4: 'D'}
d3 = {5: 'E'}
d4 = {**d1, **d2, **d3}
print(d4)
