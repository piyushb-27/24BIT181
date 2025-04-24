'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Create a vCard
name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")

with open("contact.vcf", "w") as f:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    f.write("FN:" + name + "\n")
    f.write("TEL:" + phone + "\n")
    f.write("EMAIL:" + email + "\n")
    f.write("END:VCARD\n")
