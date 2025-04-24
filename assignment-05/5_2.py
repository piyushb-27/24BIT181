'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import random

# Generate 20 random integers, find all positions of a user-input number
nums = [random.randint(1, 10) for _ in range(20)]
print("Generated list:", nums)

target = int(input("Enter number to find positions: "))
positions = []

for idx, val in enumerate(nums):
    if val == target:
        positions.append(idx)

print("Positions:", positions)
