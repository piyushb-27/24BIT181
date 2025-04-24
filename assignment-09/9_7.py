'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Palindrome
def ispalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(ispalindrome("A man a plan a canal Panama"))
