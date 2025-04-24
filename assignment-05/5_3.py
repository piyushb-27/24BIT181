'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import random

# Generate 50 random numbers in range 1-30 and remove duplicates
numbers = [random.randint(1, 30) for _ in range(50)]
print("Original list:", numbers)
unique = list(set(numbers))
print("After removing duplicates:", unique)
