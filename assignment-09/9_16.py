'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Recursive a^b
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

print(power(2, 5))
