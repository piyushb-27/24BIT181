'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Elements from list1 not in list2
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 4, 6]
list3 = [x for x in list1 if x not in list2]
print("List1:", list1)
print("List2:", list2)
print("List3 (only in List1):", list3)
