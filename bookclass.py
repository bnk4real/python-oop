class Book:
    def __init__(self,title:str, quantity:int, author:str, price:int):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
    def __str__(self):
        return f'Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}'

# Set values (consider to store data from databse or else.)
book1 = Book('Introduction to Programming', 12, 'Author 1', 120)
book2 = Book('Introduction to Python', 18, 'Author 2', 220)
book3 = Book('Introduction to Go', 15, 'Author 3', 320)

# Append to array list
bookList = [book1, book2, book3]
