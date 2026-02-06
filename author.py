# Parent Class: Book
class Book:
    def __init__(self, title, author):   # ✅ Correct constructor
        self.title = title
        self.author = author

    def display_book_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


# Child Class: IssuedBook
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):   # ✅ Correct constructor
        super().__init__(title, author)   # call parent constructor
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        # Call parent method
        self.display_book_details()
        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)


# --- Testing ---
book1 = IssuedBook ("Python Programming", "Guido van Rossum", "John Doe", "01-Feb-2026")
book1.display_issued_book_details()
