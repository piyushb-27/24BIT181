'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Remove duplicates and sort
def convert(s):
    words = s.split()
    words = sorted(set(words))
    return " ".join(words)

print(convert("pdeu ict ict rocks pdeu rocks python"))
