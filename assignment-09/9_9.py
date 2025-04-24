'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Count alphabets and digits
def count_alpha_digits(s):
    d = {"alpha": 0, "digit": 0}
    for ch in s:
        if ch.isalpha():
            d["alpha"] += 1
        elif ch.isdigit():
            d["digit"] += 1
    return d

print(count_alpha_digits("ICT2025PDEU42"))
