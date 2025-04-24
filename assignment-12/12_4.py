'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 4. Shape (circle) perimeter and area calculations
import math

class Shape:
    def __init__(self, shape="circle"):
        self.shape = shape
        self.radius = 0

    def input_data(self):
        if self.shape.lower() == "circle":
            self.radius = float(input("Enter the radius of the circle: "))
        else:
            print("Shape not supported")

    def perimeter(self):
        if self.shape.lower() == "circle":
            return 2 * math.pi * self.radius
        return 0

    def area(self):
        if self.shape.lower() == "circle":
            return math.pi * self.radius ** 2
        return 0

# Example usage
circle = Shape("circle")
circle.input_data()
print(f"Circumference of circle: {circle.perimeter()}")
print(f"Area of circle: {circle.area()}")
