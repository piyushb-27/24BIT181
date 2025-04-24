'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 2. Own functions to convert to lower/upper/toggle case
s = input("Enter a string for case conversion: ")

# Convert to uppercase
upper_str = ""
for ch in s:
    if 'a' <= ch <= 'z':
        upper_str += chr(ord(ch) - 32)
    else:
        upper_str += ch
print("uppercase:", upper_str)

# Convert to lowercase
lower_str = ""
for ch in s:
    if 'A' <= ch <= 'Z':
        lower_str += chr(ord(ch) + 32)
    else:
        lower_str += ch
print("lowercase:", lower_str)

# Toggle case
toggle_str = ""
for ch in s:
    if 'A' <= ch <= 'Z':
        toggle_str += chr(ord(ch) + 32)
    elif 'a' <= ch <= 'z':
        toggle_str += chr(ord(ch) - 32)
    else:
        toggle_str += ch
print("togglecase:", toggle_str)
