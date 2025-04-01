class Book:
    def __init__(self,name, author):
        self.name = name
        self.author = author
        self.is_checked_out = False

    def __str__(self):
        return f"'{self.name}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.name}' added to the library.")

   
    def display_books(self):
        print("\nAvailable Books:")
        available_books = [book for book in self.books if not book.is_checked_out]
        if not available_books:
            print("No available books at the moment.")
        for book in available_books:
            print(f"- {book}")

    def check_out_book(self, name):
        for book in self.books:
            if book.title.lower() == name.lower() and not book.is_checked_out:
                book.is_checked_out = True
                print(f"You have checked out '{book.name}'.")
                return
        print(f"Book '{name}' is either not available or already checked out.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. list books")
        print("3. lent book")
        choice = input("Enter your choice: ")

        if choice == '1':
            name= input("Enter book name: ")
            author = input("Enter book aging: ")
            book = Book(name, author)
            library.add_book(book)

       
        elif choice == '2':
            library.display_books()

        elif choice == '3':
            name = input("Enter the title of the book to check out: ")
            library.check_out_book(name)

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
