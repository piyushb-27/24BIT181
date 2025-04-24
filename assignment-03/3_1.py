'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 1. Count how many vowels are there in a string. Accept the string from the user.
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count = count + 1
print("vowel count:", count)
