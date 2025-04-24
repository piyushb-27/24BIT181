'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Total bill from 2 dictionaries
prices = {"rice": 60, "wheat": 40, "milk": 25}
qty = {"rice": 2, "wheat": 3, "milk": 5}
total = 0
for item in prices:
    if item in qty:
        total += prices[item] * qty[item]
print("total bill:", total)
