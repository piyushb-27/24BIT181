'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 3. Solid (cube) surface area and volume calculations
class Solid:
    def __init__(self, shape="cube"):
        self.shape = shape
        self.side = 0

    def input_data(self):
        if self.shape.lower() == "cube":
            self.side = float(input("Enter the side length of the cube: "))
        else:
            print("Shape not supported")

    def surface_area(self):
        if self.shape.lower() == "cube":
            return 6 * self.side ** 2
        return 0

    def volume(self):
        if self.shape.lower() == "cube":
            return self.side ** 3
        return 0

# Example usage
cube = Solid("cube")
cube.input_data()
print(f"Surface Area of cube: {cube.surface_area()}")
print(f"Volume of cube: {cube.volume()}")
