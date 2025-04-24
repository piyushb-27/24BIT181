'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Print palindromes only
lst = ['madam', 'Python', 'malayalam', 12321]
for item in lst:
    s = str(item)
    if s == s[::-1]:
        print(s)
