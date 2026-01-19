class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} by {book.author}")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"Book '{title}' issued successfully")
                return
        print(f"Book '{title}' is not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"Book '{title}' returned successfully")
                return
        print(f"Book '{title}' was not issued")


library = Library()

book1 = Book("Python Basics", "Guido")
book2 = Book("Data Science", "Jake")
book3 = Book("Machine Learning", "Andrew")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

library.issue_book("Python Basics")
library.display_books()

library.return_book("Python Basics")
library.display_books()
