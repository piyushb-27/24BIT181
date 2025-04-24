'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# compute n + nn + nnn + nnnn
def compute(n):
    n = str(n)
    return int(n) + int(n*2) + int(n*3) + int(n*4)

for i in range(4, 8):
    print(i, "->", compute(i))
