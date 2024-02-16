from bookclass import *

# bookstore class

print("Welcome to Bookstore.")
inputBook = input("Enter Book Name: ")

while inputBook.lower() != "no":
    book_found = False
    
    for x in bookList:
        if inputBook.lower() == x.title.lower():
            print("You selected", x.title)
            inputQty = int(input("Enter Qty: "))
            if inputQty > x.quantity:
                print("Book:", x.title, "is Out of Stock.")
            else:
                print("You've selected:", x.title, "Thank you!")
            book_found = True
            break
    
    if not book_found:
        print("Book not found in the list.")
    
    inputBook = input("Enter Book Name (or 'no' to exit): ")

print("Thank you!")

# simplest ways
# if inputBook == "1":
#     print("You've selected :", book1.title)
#     inputQty = int(input("Enter Qty: "))
#     if inputQty > book1.quantity:
#         print("Book:", book1.title, "is Out of Stock.")
#     else:
#         print("You've selected :", book1.title, "Thank you!")
# elif inputBook == "2":
#     print("You've selected :", book2.title)
#     inputQty = int(input("Enter Qty: "))
#     if inputQty > book2.quantity:
#         print("Book:", book2.title, "is Out of Stock.")
#     else:
#         print("You've selected :", book2.title, "Thank you!")
# elif inputBook == "3":
#     print("You've selected :", book3.title)
#     inputQty = int(input("Enter Qty: "))
#     if inputQty > book2.quantity:
#         print("Book:", book1.title, "is Out of Stock.")
#     else:
#         print("You've selected :", book3.title, "Thank you!")
