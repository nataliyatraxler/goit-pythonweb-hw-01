import logging
from abc import ABC, abstractmethod
from typing import List

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Принцип SRP: окремий клас для зберігання інформації про книгу
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def __str__(self) -> str:
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

# Принцип ISP: створюємо інтерфейс для бібліотеки
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass

# Принцип LSP: клас Library реалізує інтерфейс, щоб його можна було замінити іншими реалізаціями
class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f'Book added: {book}')

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]
        logging.info(f'Book removed: {title}')

    def show_books(self) -> None:
        if not self.books:
            logging.info("Library is empty.")
        else:
            for book in self.books:
                logging.info(book)

# Принцип DIP: LibraryManager залежить від абстракції LibraryInterface
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()

# Основний цикл програми
def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command: str = input("Enter command (add, remove, show, exit): ").strip().lower()
        
        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: int = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.warning("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
