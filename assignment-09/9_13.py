'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Binary equivalent
def binary(n):
    if n == 0:
        return ""
    else:
        return binary(n // 2) + str(n % 2)

print(binary(25))
