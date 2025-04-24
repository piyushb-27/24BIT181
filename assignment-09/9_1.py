'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Count lowercase and uppercase
def count_lower# Count lowercase and uppercase
def count_lower_upper(s):
    d = {"lower": 0, "upper": 0}
    for ch in s:
        if ch.islower():
            d["lower"] += 1
        elif ch.isupper():
            d["upper"] += 1
    return d

print(count_lower_upper("PDEU Rocks at ICT Dept"))
