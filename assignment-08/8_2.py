'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import random

# 10 random numbers in range 15–45, count <30, delete >35
nums = set()
while len(nums) < 10:
    nums.add(random.randint(15, 45))
print(nums)

count = 0
for n in nums:
    if n < 30:
        count += 1
print("count <", count)

to_remove = {n for n in nums if n > 35}
nums -= to_remove
print(nums)
