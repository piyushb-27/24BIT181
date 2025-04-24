'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Create 3D array
def create_array(x, y, z, val):
    return [[[val for _ in range(z)] for _ in range(y)] for _ in range(x)]

arr = create_array(2, 2, 2, 7)
print(arr)
