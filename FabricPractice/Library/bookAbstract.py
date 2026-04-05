from abc import ABC, abstractmethod

class Book(ABC): 
    def __init__(self, title: str, author: str, price: float):
        self._title = title
        self._author = author
        self._price = price

    @abstractmethod
    def get_title():
        pass
    @abstractmethod
    def get_author():
        pass
    @abstractmethod
    def get_price():
        pass
    @abstractmethod
    def get_info():
        pass

    
    
