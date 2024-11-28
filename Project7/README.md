Library Management System
This program allows users to add, view, and search for books in a library. The Book class represents a book with its name and author, while the main system provides an interactive menu for users.

Main Features:
Add Book: Allows users to add a book with a title and author.
View Books: Displays all books in the library.
Search Book: Lets users search for a book by its name.
Exit: Ends the program.

Algorithms Used:
Adding a Book:
The program adds a book to the books list when the user inputs a book name and author.

Viewing Books:
The program iterates through the books list and displays each book's name and author.

Searching for a Book:
The program iterates through the books list to search for a book by name. If the book is found, it displays the book's details; otherwise, it informs the user that the book isn't found.
Menu Selection:

The program uses a loop to continuously display the menu options and accept the user's choice. The program executes the appropriate action based on the user's input, ensuring that invalid options prompt the user to select again.
Example:
if __name__ == "__main__":
    menu()
