# library.py
# Author: Amit Jatthap | Date: 30-Nov-2025
# Assignment 03 - Library Management

import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()

    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
        self.save_data()

    def lend_book(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)

        if member and book:
            if member.borrow_book(book):
                print(f"{member.name} borrowed '{book.title}'.")
                self.save_data()
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid book or member.")

    def take_return(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)

        if member and book:
            if member.return_book(book):
                print(f"Book '{book.title}' returned successfully.")
                self.save_data()
            else:
                print("This member didn't borrow this book.")
        else:
            print("Invalid details.")

    def get_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def get_member(self, member_id):
        for mem in self.members:
            if mem.member_id == member_id:
                return mem
        return None

    def save_data(self):
        with open("books.json", "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

        with open("members.json", "w") as f:
            json.dump([m.to_dict() for m in self.members], f, indent=4)

    def load_data(self):
        try:
            with open("books.json", "r") as f:
                self.books = [Book.from_dict(b) for b in json.load(f)]

            with open("members.json", "r") as f:
                self.members = [Member.from_dict(m) for m in json.load(f)]

        except:
            self.books = []
            self.members = []

    def library_report(self):
        borrowed_count = sum(not b.available for b in self.books)
        print("\n===== Library Report =====")
        print(f"Total Books: {len(self.books)}")
        print(f"Borrowed Books: {borrowed_count}")
        print(f"Active Members: {len(self.members)}")
        print("==========================\n")
