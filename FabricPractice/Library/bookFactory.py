from bookAbstract import Book
from books import ScienceBook, FictionalBook, ArtBook
from typing import Type

class BookFactory:
    _book_types: dict[str, Type[Book]] = {
        "fiction": FictionalBook,
        "science": ScienceBook,
        "art": ArtBook
    }

    @classmethod
    def create_book(cls, book_type: str, title: str, author: str, price: float, **kwargs):
        book_type_lowercase = book_type.lower()

        if book_type_lowercase not in book_type_lowercase:
            raise ValueError(
                f"book type is unknown {book_type}"
            )
        
        book_class = cls._book_types[book_type_lowercase]
        return book_class(title=title, author=author, price=price, **kwargs
        )
    
    @classmethod
    def book_reg(cls, type_name: str, book_class: Type[Book]):
        if not issubclass(book_class, Book):
            raise TypeError(f'{book_class.__name__} не наследник класса Book')
        cls._book_types[type_name.lower()] = book_class

    