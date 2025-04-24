'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Three functions in a list
def fun():
    print("fun called")
def disp():
    print("disp called")
def msg():
    print("msg called")

lst = [fun, disp, msg]
for f in lst:
    f()
