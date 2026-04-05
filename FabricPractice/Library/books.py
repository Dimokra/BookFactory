from py.FabricPractice.Library.bookAbstract import Book
class FictionalBook(Book):
    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_price(self):
        return self._price
    def get_info(self):
        return (
            f'Фантастика, {self._title, ' ', self._author, " ", self._price}'
        )
class ScienceBook(Book):
    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_price(self):
        return self._price
    def get_info(self):
        return (
            f'Научная, {self._title, ' ', self._author, " ", self._price}'
        )
class ArtBook(Book):
    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_price(self):
        return self._price
    def get_info(self):
        return (
            f'Исскуство, {self._title, ' ', self._author, " ", self._price}'
        )