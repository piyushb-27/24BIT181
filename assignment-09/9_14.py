'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Recursive vowel count
def count_vowels(s):
    if not s:
        return 0
    if s[0].lower() in "aeiou":
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

print(count_vowels("PDEU Rocks With Energy"))
