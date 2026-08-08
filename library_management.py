class Book:
    def __init__(self, book_id, title, author, price, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.category = category  

    def display(self):
        print(f"Book ID  : {self.book_id}")
        print(f"Title : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Price : {self.price}")
        print(f"Category : {self.category}")
        print(f"\n")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!\n")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nLibrary Book Records")
            for book in self.books:
                book.display()

library = Library()

while True:
    print("\nLibrary Book Management System")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        price = float(input("Enter Price: "))

        print("Category:")
        print("1. Premium")
        print("2. Standard")
        cat_choice = int(input("Enter category choice: "))

        if cat_choice == 1:
            category = "Premium"
        else:
            category = "Standard"

        book = Book(book_id, title, author, price, category)
        library.add_book(book)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        print("Thank you for using Library Book Management System.")
        break

    else:
        print("Invalid choice! Please try again.")
