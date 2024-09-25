class Book:
    def __init__(self, name, author, genre, price):
        self.__name = name
        self.__author = author
        self.__genre = genre
        self.__price = price

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_price(self):
        return self.__price

    def display_info(self):
        return f"Name: {self.__name}, Author: {self.__author}, Genre: {self.__genre}, Price: {self.__price}"


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.get_name()}' added to the library.")

    def delete_book(self, book_name):
        for book in self.books:
            if book.get_name() == book_name:
                self.books.remove(book)
                print(f"Book '{book_name}' removed from the library.")
                return
        print(f"Book '{book_name}' not found.")

    def search_book(self, book_name):
        for book in self.books:
            if book.get_name() == book_name:
                print("Book found:")
                print(book.display_info())
                return book
        print(f"Book '{book_name}' not found.")
        return None

    def borrow_book(self, user, book_name):
        book = self.search_book(book_name)
        if book and book_name not in self.borrowed_books:
            self.borrowed_books[book_name] = user.get_username()
            print(f"Book '{book_name}' borrowed by {user.get_username()}")
        else:
            print(f"Book '{book_name}' is already borrowed.")

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            del self.borrowed_books[book_name]
            print(f"Book '{book_name}' returned to the library.")
        else:
            print(f"Book '{book_name}' was not borrowed.")


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.borrowed_books = []

    def get_username(self):
        return self.__username

    def register(self, user_list):
        if self.__username not in user_list:
            user_list[self.__username] = self.__password
            print(f"User '{self.__username}' registered successfully.")
        else:
            print(f"User '{self.__username}' already exists.")

    def login(self, user_list):
        if self.__username in user_list and user_list[self.__username] == self.__password:
            print(f"User '{self.__username}' logged in successfully.")
            return True
        else:
            print(f"Login failed for user '{self.__username}'.")
            return False


library = Library()

book1 = Book("Harry Potter", "J.K. Rowling", "Fantasy", 20)
book2 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 15)

library.add_book(book1)
library.add_book(book2)

user_list = {}
user1 = User("john_smith", "password123")

user1.register(user_list)
if user1.login(user_list):
    library.borrow_book(user1, "Harry Potter")
    library.return_book("Harry Potter")
