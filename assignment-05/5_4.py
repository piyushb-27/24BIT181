'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import random

# 30 random numbers split into positive and negative lists
mixed = [random.randint(-50, 50) for _ in range(30)]
positives = []
negatives = []

for n in mixed:
    if n >= 0:
        positives.append(n)
    else:
        negatives.append(n)

print("Original:", mixed)
print("Positives:", positives)
print("Negatives:", negatives)
