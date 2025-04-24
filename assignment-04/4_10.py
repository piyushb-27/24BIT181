'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 10. Fibonacci series
N = int(input("Enter how many Fibonacci numbers: "))
a = 0
b = 1
print(a, end=' ')
if N > 1:
    print(b, end=' ')
for i in range(2, N):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
print()
