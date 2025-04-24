'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Delete an element of a tuple

original_tuple = (5, 10, 15, 20)

# Convert to list
temp_list = list(original_tuple)

# Delete the 3rd element (index 2)
del temp_list[2]

# Convert back to tuple
new_tuple = tuple(temp_list)

print("Tuple after deleting an element:", new_tuple)
