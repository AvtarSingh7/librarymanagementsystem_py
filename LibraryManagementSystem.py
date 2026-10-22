
books = ["Python", "Computer", "English"]

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. View available books")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Add a new book")
    print("5. Remove a book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Available books:", books)

    elif choice == "2":
        book = input("Enter book name: ")
        if book in books:
            books.remove(book)
            print("Book issued successfully!")
        else:
            print("Book not available.")

    elif choice == "3":
        book = input("Enter book name: ")
        books.append(book)
        print("Book returned successfully!")

    elif choice == "4":
        book = input("Enter new book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "5":
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found.")

    elif choice == "6":
        print("Thank you for using the library!")
        break

    else:
        print("Invalid choice. Try again.")
        