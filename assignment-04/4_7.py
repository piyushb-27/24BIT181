'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 7. nCr and nPr
n = int(input("Enter n: "))
r = int(input("Enter r: "))

nf = 1
for i in range(1, n + 1):
    nf *= i

rf = 1
for i in range(1, r + 1):
    rf *= i

nrf = 1
for i in range(1, n - r + 1):
    nrf *= i

nCr = nf // (rf * nrf)
nPr = nf // nrf

print("nCr:", nCr)
print("nPr:", nPr)
