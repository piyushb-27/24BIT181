'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 6. 24 Hours with suffix
for h in range(0, 24):
    if h == 0:
        print("12 Midnight")
    elif h < 12:
        print(h, "AM")
    elif h == 12:
        print("12 Noon")
    else:
        print(h - 12, "PM")
