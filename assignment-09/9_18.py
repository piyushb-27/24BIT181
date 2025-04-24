'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Average of list recursively
def avg_recursive(lst, i=0, total=0):
    if i == len(lst):
        return total / len(lst)
    return avg_recursive(lst, i + 1, total + lst[i])

print(avg_recursive([10, 20, 30, 40, 50]))
