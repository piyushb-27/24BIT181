'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Remove empty tuples from a list

tuples_list = [(), (1, 2), (), (3, 4, 5), (), ("a", "b")]

filtered_list = []

for tup in tuples_list:
    if tup != ():
        filtered_list.append(tup)

print("List after removing empty tuples:", filtered_list)
