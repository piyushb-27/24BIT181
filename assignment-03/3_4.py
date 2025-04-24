'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 4. Remove one string from another if present
one = input("Enter the main string: ")
remove = input("Enter the string to remove: ")

final = ""
i = 0
while i < len(one):
    if one[i:i+len(remove)] == remove:
        i += len(remove)
    else:
        final += one[i]
        i += 1
print("final string:", final)
