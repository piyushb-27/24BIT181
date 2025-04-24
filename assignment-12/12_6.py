'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 6. Date comparison with overloaded == operator
class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date

    def __str__(self):
        return f"{self.date[0]:02d}/{self.date[1]:02d}/{self.date[2]}"

# Example usage
d1 = Date(15, 8, 2023)
d2 = Date(15, 8, 2023)
d3 = Date(20, 4, 2025)
print(f"Date 1: {d1}")
print(f"Date 2: {d2}")
print(f"Date 3: {d3}")
print(f"Date 1 == Date 2: {d1 == d2}")
print(f"Date 1 == Date 3: {d1 == d3}")
