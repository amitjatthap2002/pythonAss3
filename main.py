# main.py
# Assignment 03 - Interactive Menu
from library import Library

lib = Library()

print("\n===== Welcome to Library System =====\n")

while True:
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Library Report")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        lib.add_book(input("Title: "), input("Author: "), input("ISBN: "))
    elif choice == "2":
        lib.register_member(input("Name: "), input("Member ID: "))
    elif choice == "3":
        lib.lend_book(input("Member ID: "), input("ISBN: "))
    elif choice == "4":
        lib.take_return(input("Member ID: "), input("ISBN: "))
    elif choice == "5":
        lib.library_report()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice, try again.")
