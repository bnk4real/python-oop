from usersclass import *

print("Employees Mock Database")
findInput = input("Enter User ID:")

while findInput.lower() != "no":
    is_found = False 
    for users in userList:
        if findInput == users.id:
            print("Found user ID:", users.id, "Name:", users.name, "Position:", users.position)
    findInput = input("Enter User ID: (Or enter 'no' to exit.)")

    if not is_found:
        print("No data found.")

print("Have a good one!")