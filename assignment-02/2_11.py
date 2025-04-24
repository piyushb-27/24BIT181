'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 11. Check if 3 points lie on a straight line
x1, y1 = 0, 0
x2, y2 = 2, 2
x3, y3 = 4, 4
if (y2 - y1)*(x3 - x2) == (y3 - y2)*(x2 - x1):
    print("straight line")
else:
    print("not on line")
