'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 3. Count alphabets and digits in string
s = input("Enter a string: ")
alpha = 0
digit = 0
for ch in s:
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        alpha += 1
    elif '0' <= ch <= '9':
        digit += 1
print("alphabets:", alpha)
print("digits:", digit)
