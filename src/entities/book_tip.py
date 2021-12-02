import re

class BookTip:
    def __init__(self, name: str, author: str, isbn: str, publication_year: str, id_number: int = None, read: bool = False):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.id_number = id_number
        self.read = read

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
        if len(value) <= 0 or len(value) > 20:
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
            raise ValueError("Vuosi pitää olla välillä 0-3000")
        self.__publication_year = value

    def __str__(self):
        pad = 7

        return f"{'Index:':{pad}} {self.id_number}\n" \
                f"{'Read:':{pad}} {self.read}\n" \
                f"{'Title:':{pad}} {self.name}\n" \
                f"{'Author:':{pad}} {self.author}\n" \
                f"{'ISBN:':{pad}} {self.isbn}\n" \
                f"{'Year:':{pad}} {self.publication_year}\n"

    def __eq__(self, other: object) -> bool:

        if isinstance(other, BookTip):
            return self.name == other.name\
                and self.author == other.author\
                and self.isbn == other.isbn\
                and self.publication_year == other.publication_year

        return False
