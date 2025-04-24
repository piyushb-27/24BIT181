'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 12. Point inside/on/outside circle
import math
x, y = 3, 4
center_x, center_y = 0, 0
radius = 5
distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
if distance < radius:
    print("inside")
elif distance == radius:
    print("on")
else:
    print("outside")
