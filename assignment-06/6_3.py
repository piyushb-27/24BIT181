'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

from datetime import date

# Find number of days between two date tuples

date1 = (12, 4, 2023)  # 12 April 2023
date2 = (20, 4, 2025)  # 20 April 2025

d1 = date(date1[2], date1[1], date1[0])  # (year, month, day)
d2 = date(date2[2], date2[1], date2[0])

difference = d2 - d1
print("Number of days between two dates:", difference.days)
