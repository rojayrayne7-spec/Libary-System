from datetime import date, timedelta
from enum import Enum

class BookStatus(Enum):
    AVAILABLE = "Available"
    BORROWED = "Borrowed"
    RESERVED = "Reserved"


class Book:
    def __init__(self, isbn: str, title: str, author: str, status=BookStatus.AVAILABLE):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__status = status

    def get_isbn(self) -> str:
        return self.__isbn

    def get_status(self) -> BookStatus:
        return self.__status

    def set_status(self, status: BookStatus):
        self.__status = status

    def is_available(self) -> bool:
        return self.__status == BookStatus.AVAILABLE

    def __repr__(self):
        return f"{self.__title} by {self.__author} ({self.__status.value})"


class Loan:
    def __init__(self, loan_id: str, loan_date: date, due_date: date):
        self.__loan_id = loan_id
        self.__loan_date = loan_date
        self.__due_date = due_date
        self.__return_date = None

    def close_loan(self, return_date: date):
        self.__return_date = return_date

    def is_overdue(self, current_date: date) -> bool:
        return self.__return_date is None and current_date > self.__due_date


class Reservation:
    def __init__(self, reservation_id: str, request_date: date, expiry_days: int = 3):
        self.__reservation_id = reservation_id
        self.__request_date = request_date
        self.__expiry_date = request_date + timedelta(days=expiry_days)

    def is_expired(self, current_date: date) -> bool:
        return current_date > self.__expiry_date

    def cancel(self):
        print(f"Reservation {self.__reservation_id} cancelled.")

class LibraryCatalog:
    def __init__(self):
        self._books=()


    def add_book(self, book: Book):
        self.__books[book.get_isbn()] = book

    def remove_book(self, isbn: str):
        if isbn in self.__books:
            del self.__books[isbn]

    def search_books(self, query: str):
        return [b for b in self.__books.values()
                if query.lower() in b._Book__title.lower() or query.lower() in b._Book__author.lower()]

    def list_available_books(self):
        return [b for b in self.__books.values() if b.is_available()]


class User:
    def __init__(self, user_id: str, name: str, email: str, password_hash: str):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._password_hash = self._password_hash

    def login(self, email: str, password_hash: str) -> bool:
        return self._email == email and self._password_hash == password_hash

    def get_role(self) -> str:
        return "User" 


class Member(User):
    def __init__(self, user_id, name, email, password_hash, max_borrow_limit=5):
        super().__init__(user_id, name, email, password_hash)
        self.__borrowed_books = []
        self.__max_borrow_limit = max_borrow_limit

    def borrow_book(self, book: Book):
        if len(self.__borrowed_books) >= self.__max_borrow_limit:
            print("Cannot borrow more books – limit reached.")
            return
        if not book.is_available():
            print("This book is not available.")
            return
        book.set_status(BookStatus.BORROWED)
        self.__borrowed_books.append(book)
        print(f"{self._name} borrowed {book}.")

    def return_book(self, book: Book):
        if book in self.__borrowed_books:
            book.set_status(BookStatus.AVAILABLE)
            self.__borrowed_books.remove(book)
            print(f"{self._name} returned {book}.")

    def get_role(self):
        return "Member"


class Librarian(User):
    def __init__(self, user_id, name, email, password_hash):
        super().__init__(user_id, name, email, password_hash)

    def add_book(self, catalog: LibraryCatalog, book: Book):
        catalog.add_book(book)
        print(f"Librarian added book: {book}")

    def remove_book(self, catalog: LibraryCatalog, isbn: str):
        catalog.remove_book(isbn)
        print(f"Librarian removed book with ISBN {isbn}")

    def get_role(self):
        return "Librarian"


class Administrator(User):
    def __init__(self, user_id, name, email, password_hash):
        super().__init__(user_id, name, email, password_hash)
        self.__borrow_limit = 5
        self.__penalty_rate = 1.0

    def set_borrow_limit(self, limit: int):
        self.__borrow_limit = limit
        print(f"Borrow limit set to {limit}")

    def set_late_penalty(self, rate: float):
        self.__penalty_rate = rate
        print(f"Late penalty set to {rate}/day")

    def get_role(self):
        return "Administrator"
    
    if __name__=="__main__":
       book= Book("123","Python Programming","John Smith")
    print(book)
    if book.is_available():
      print("Book is available")
