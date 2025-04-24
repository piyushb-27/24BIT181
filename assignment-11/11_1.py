'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Asks user to enter an integer and if string is entered then validates the error.

while True:
    try:
        user_input = input("Please enter an integer: ")
        number = int(user_input)
        print(f"integer received: {number}")
        break
    except ValueError:
        print("Error: Please enter a valid integer, not a string or other characters.")