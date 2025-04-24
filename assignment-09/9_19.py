'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Recursive string length
def str_len(s):
    if s == "":
        return 0
    return 1 + str_len(s[1:])

print(str_len("PDEU"))
