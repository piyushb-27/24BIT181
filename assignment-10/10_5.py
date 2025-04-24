'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Copy file & convert lowercase to uppercase
with open("source.txt", "w") as f:
    f.write("Pdeu\n")

with open("source.txt", "r") as f1, open("upper.txt", "w") as f2:
    for line in f1:
        f2.write(line.upper())
