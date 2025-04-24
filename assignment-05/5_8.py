'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

from collections import deque

# Queue - Menu-driven
queue = deque()

while True:
    print("\nQueue Menu\n1. Insert\n2. Delete\n3. Display\n4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        val = input("Enter value to insert: ")
        queue.append(val)
    elif choice == '2':
        if queue:
            print("Deleted:", queue.popleft())
        else:
            print("Queue is empty.")
    elif choice == '3':
        print("Queue contents:", list(queue))
    elif choice == '4':
        break
    else:
        print("Invalid")
