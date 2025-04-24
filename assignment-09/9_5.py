'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Pangram
def ispangram(s):
    s = s.lower()
    return set("abcdefghijklmnopqrstuvwxyz") <= set(s)

print(ispangram("The quick brown fox jumps over the lazy dog"))
