'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Filter names with length > 8
names = ["Ravi", "Shantanu", "Bhargav", "Madhusudan", "Priyanka", "Anand", "Udaybhanu"]
long_names = list(filter(lambda x: len(x) > 8, names))
print(long_names)
