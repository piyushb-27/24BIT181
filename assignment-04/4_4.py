'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 4. Check prime, perfect, Armstrong, palindrome, automorphic
n = int(input("Enter a number: "))

# Prime
prime = True
if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
if prime:
    print("prime")
else:
    print("not prime")

# Perfect number
sum_div = 0
for i in range(1, n):
    if n % i == 0:
        sum_div += i
if sum_div == n:
    print("perfect")
else:
    print("not perfect")

# Armstrong
temp = n
arm = 0
while temp > 0:
    d = temp % 10
    arm += d ** 3
    temp //= 10
if arm == n:
    print("armstrong")
else:
    print("not armstrong")

# Palindrome
original = n
rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10
if original == rev:
    print("palindrome")
else:
    print("not palindrome")

# Automorphic
num = original
square = num * num
if str(square).endswith(str(num)):
    print("automorphic")
else:
    print("not automorphic")
