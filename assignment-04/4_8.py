'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 8. Factorial of a given number
num = int(input("Enter number to find factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("factorial:", fact)
