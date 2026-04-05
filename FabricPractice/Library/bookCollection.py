from bookAbstract import Book
from typing import List

class BookCollection(Book):
    def __init__(self, theme: str = "without a theme"):
        self._books: List[Book] = []
        self._theme: str = theme
        self.custom_price: float  = 0.0
    
    def get_title(self) -> str:
        return self._theme

    def get_authors(self):
        authors = [book.get_author() for book in self._books]
        return ','.join(set(authors))
    
    def get_price(self) -> float:
        if self.custom_price > 0:
            return self.custom_price
        return sum(book.get_price() for book in self.books)

    def get_info(self) -> str:
        info = f'{self.theme}, {self.get_price()}, {len(self.books)},\n  '
        for book in self.books:
            info += f"  - {book.get_title()} ({book.get_author()}) - {book.get_price()}\n"
        return info

class BookCollectionBuilder:
    def __init__(self):
        self._bookcollection = BookCollection()

    def add_book(self, book: Book):
        self.collection.books.append(book)
        return self

    def set_theme(self, theme: str):
        self.collection.theme = theme
        return self

    def set_price(self, price: float = 0.0):
        self.collection.custom_price = price
        return self

    def build(self) -> BookCollection:
        return self.collection
    