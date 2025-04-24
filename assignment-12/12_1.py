'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 1. Complex number operations (addition, subtraction)
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
c1 = Complex(3, 4)
c2 = Complex(1, 2)
print(f"Complex number 1: {c1}")
print(f"Complex number 2: {c2}")
print(f"Addition: {c1 + c2}")
print(f"Subtraction: {c1 - c2}")
