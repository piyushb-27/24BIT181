'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import random

# Create list of 5 odd + 4 even integers using random
odds = [random.randrange(1, 100, 2) for _ in range(5)]
print("Odd integers:", odds)

evens = [random.randrange(0, 100, 2) for _ in range(4)]
print("Even integers:", evens)

odds[2] = evens
print("Replaced 3rd odd element with even list:", odds)

# Flattening
flat = []
for item in odds:
    if isinstance(item, list):
        flat.extend(item)
    else:
        flat.append(item)

print("Flattened list:", flat)

flat.sort()
print("Sorted list:", flat)
