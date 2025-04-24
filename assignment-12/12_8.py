'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 8. String operations (concatenation, case conversion)
class String:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other.value
        return self

    def toLower(self):
        return String(self.value.lower())

    def toUpper(self):
        return String(self.value.upper())

    def __str__(self):
        return self.value

# Example usage
s1 = String("Hello")
s2 = String("World")
print(f"String 1: {s1}")
print(f"String 2: {s2}")
s1 += s2
print(f"After concatenation: {s1}")
print(f"Lowercase: {s1.toLower()}")
print(f"Uppercase: {s1.toUpper()}")
