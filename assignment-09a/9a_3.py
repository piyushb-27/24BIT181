'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import random

# 10 random numbers between -15 and 15, get their squares
nums = random.sample(range(-15, 16), 10)
squares = list(map(lambda x: x**2, nums))
print(nums)
print(squares)
