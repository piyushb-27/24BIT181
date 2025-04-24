'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Merge lines alternatively
with open("file1.txt", "w") as f:
    f.write("Line1-A\nLine2-A\nLine3-A\n")
with open("file2.txt", "w") as f:
    f.write("Line1-B\nLine2-B\n")

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
f3 = open("merged.txt", "w")

lines1 = f1.readlines()
lines2 = f2.readlines()

i = 0
while i < len(lines1) or i < len(lines2):
    if i < len(lines1):
        f3.write(lines1[i])
    if i < len(lines2):
        f3.write(lines2[i])
    i += 1

f1.close()
f2.close()
f3.close()
