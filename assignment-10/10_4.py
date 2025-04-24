'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import os, shutil

# Create subdir and copy file into it
if not os.path.exists("newdir"):
    os.mkdir("newdir")

if not os.path.exists("sourcedir"):
    os.mkdir("sourcedir")

with open("sourcedir/sample.txt", "w") as f:
    f.write("Hello from PDEU!")

shutil.copy("sourcedir/sample.txt", "newdir/sample.txt")
