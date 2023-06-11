class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.is_available = False
                print(f"Book with ID {book_id} has been borrowed.")
                return
        print(f"Book with ID {book_id} is not available for borrowing.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_available:
                book.is_available = True
                print(f"Book with ID {book_id} has been returned.")
                return
        print(f"Invalid book ID or book is already available.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                if book.is_available:
                    print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

# Create a library object
library = Library()

# Add some books to the library
book1 = Book(1, "Python Programming", "John Smith")
book2 = Book(2, "Data Science 101", "Jane Doe")
book3 = Book(3, "Algorithms and Data Structures", "David Johnson")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display available books
library.display_books()

# Borrow a book
library.borrow_book(2)

# Display available books again
library.display_books()

# Return a book
library.return_book(2)

# Display available books after returning a book
library.display_books()
