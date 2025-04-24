'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Reverse list recursively
def reverse_list(l):
    if len(l) == 0:
        return []
    return [l[-1]] + reverse_list(l[:-1])

print(reverse_list([1, 2, 3, 4, 5]))
