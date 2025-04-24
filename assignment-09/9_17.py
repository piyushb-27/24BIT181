'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Replace negative with 0
def sanitize(lst, i=0):
    if i == len(lst):
        return lst
    if lst[i] < 0:
        lst[i] = 0
    return sanitize(lst, i + 1)

lst = [-2, 3, -5, 6, -1]
print(sanitize(lst))
