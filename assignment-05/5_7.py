'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Stack - Menu-driven
stack = []

while True:
    print("\nStack Menu\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        val = input("Enter value to push: ")
        stack.append(val)
    elif choice == '2':
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty.")
    elif choice == '3':
        print("Stack contents:", stack)
    elif choice == '4':
        break
    else:
        print("Invalid")
