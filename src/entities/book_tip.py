import re

class BookTip:
    def __init__(self, name: str, author: str, isbn: str, publication_year: str):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nimen pitää olla merkkijono")
        if len(value) <= 0 or len(value) > 100:
            raise ValueError("Nimen pituus pitää olla 1-100 merkkiä")
        self.__name = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Nimen pitää olla merkkijono")
        if len(value) <= 0 or len(value) > 100:
            raise ValueError("Nimen pituus pitää olla 1-100 merkkiä")
        self.__author = value

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str):
            raise TypeError("ISBN pitää olla merkkijono")
        if len(value) <= 0 and len(value) > 20:
            raise ValueError("ISBN pituus pitää olla 1-20 merkkiä")
        pattern = re.compile('^[1234567890-]+$')
        if not re.search(pattern, value):
            raise ValueError("ISBN pitää sisältää vain merkkejä 0-9 ja -")
        self.__isbn = value

    @property
    def publication_year(self):
        return self.__publication_year

    @publication_year.setter
    def publication_year(self, value):
        if not isinstance(value, str):
            raise TypeError("Vuosi pitää olla merkkijono")
        pattern = re.compile('^[1234567890]+$')
        if not re.search(pattern, value):
            raise ValueError("Vuosi pitää sisältää vain merkkejä 0-9")
        year = int(value)
        if year < 0 or  year > 3000:
            raise ValueError("Vuosi pitää olla välillä 0-300")
        self.__publication_year = value

    def __str__(self):
        return f"Book name: {self.name}\n" \
                f"Author: {self.author}\n" \
                f"ISBN: {self.isbn}\n" \
                f"Publication year: {self.publication_year}"
