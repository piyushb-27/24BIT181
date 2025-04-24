'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Modify an element of a tuple

original_tuple = (10, 20, 30)

# Convert to list
temp_list = list(original_tuple)

# Modify the second element
temp_list[1] = 99

# Convert back to tuple
modified_tuple = tuple(temp_list)

print("Modified tuple:", modified_tuple)
