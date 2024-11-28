# The Book class represents a single book
class Book:
    def __init__(self, name, author):
        self.name = name  # The name of the book
        self.author = author  # The author of the book

# Function to display the menu options and perform actions
def menu():
    books = []  # Empty list to store the books
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            # Add book
            name = input("Enter the book name: ")
            author = input("Enter the author's name: ")
            new_book = Book(name, author)
            books.append(new_book)
            print(f"Book '{name}' by {author} added to the library.")
        
        elif choice == "2":
            # View all books
            if len(books) == 0:
                print("No books in the library.")
            else:
                print("\nBooks in the library:")
                for book in books:
                    print(f"{book.name} by {book.author}")
        
        elif choice == "3":
            # Search for a book
            search_name = input("Enter the book name to search: ")
            found = False
            for book in books:
                if book.name.lower() == search_name.lower():
                    print(f"Found: {book.name} by {book.author}")
                    found = True
                    break
            if not found:
                print("Book not found!")
        
        elif choice == "4":
            # Exit the program
            print("Exiting the library system...")
            break
        
        else:
            print("Invalid option! Please choose a valid option (1-4).")

# Run the program
if __name__ == "__main__":
    menu()
