'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 11. sin(x) using series
x_deg = float(input("Enter angle in degrees: "))
x = x_deg * 3.14159 / 180

terms = 10
sinx = 0
sign = 1
for i in range(1, 2 * terms, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sinx += sign * (x ** i) / fact
    sign *= -1
print("sin(x):", sinx)
