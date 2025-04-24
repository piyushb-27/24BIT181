'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Frequency of words
def frequency(s):
    s = s.lower().split()
    d = {}
    for word in s:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return dict(sorted(d.items()))

print(frequency("the quick brown fox jumps over the lazy dog the quick fox"))
