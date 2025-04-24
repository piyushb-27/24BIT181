'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Recursive Prime Factors
def prime_factors(n, i=2):
    if i > n:
        return
    if n % i == 0:
        print(i)
        return prime_factors(n // i, i)
    else:
        return prime_factors(n, i + 1)

prime_factors(180)
