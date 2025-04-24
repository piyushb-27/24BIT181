'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 3. Accept two strings. Check whether one string is there in another string.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 in s2:
    print("present")
elif s2 in s1:
    print("present")
else:
    print("not present")
