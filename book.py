# book.py
# Author: Amit Jatthap | Date: 30-Nov-2025
# Assignment 03 - Book Class

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # default

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(data["title"], data["author"], data["isbn"])
        book.available = data["available"]
        return book
