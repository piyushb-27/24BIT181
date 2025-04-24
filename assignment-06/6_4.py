'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Sort list of food items by price in descending order

food_items = [
    ("Samosa", 20),
    ("Pizza", 150),
    ("Burger", 90),
    ("Vada Pav", 15),
    ("Dosa", 50)
]

sorted_items = sorted(food_items, key=lambda x: x[1], reverse=True)

print("Sorted food items by price (descending):")
for item in sorted_items:
    print(item)
