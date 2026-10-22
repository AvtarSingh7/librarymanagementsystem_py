# Library Management System

A Python-based Library Management System designed to manage basic library operations through a menu-driven command-line interface.

## Features

- **View Books:** Display the available books in the library.
- **Issue Books:** Issue a book from the available collection.
- **Return Books:** Add returned books back to the collection.
- **Add Books:** Add new books to the library.
- **Remove Books:** Remove books from the collection.
- **Interactive Menu:** Navigate through library operations using numbered options.

## Technologies Used

- Python 3

## Concepts Implemented

- Lists and list operations
- Loops and conditional statements
- User input and output
- List methods such as `append()` and `remove()`

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python LibraryManagementSystem.py
```

## Limitations

- Book records are stored in memory and reset when the program terminates.
- The system does not maintain borrower details or permanent transaction records.
- Book returns are not validated against previous issue transactions.

## Future Improvements

- Persistent storage using files or a database.
- Borrower registration and transaction tracking.
- Improved validation and book availability management.
- A graphical user interface.

## Purpose

This project demonstrates the application of Python programming concepts to a practical library management scenario.
