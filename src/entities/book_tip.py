class BookTip:
    def __init__(self, name: str, author: str, ISBN: str, publication_year: str):
        self.name = name
        self.author = author
        self.ISBN = ISBN
        self.publication_year = publication_year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 0 and len(value) < 100:
            self.__name = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if len(value) > 0 and len(value) < 100:
            self.__author = value

    @property
    def ISBN(self):
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, value):
        if len(value) > 0 and len(value) < 20:
            self.__ISBN = value

    @property
    def publication_year(self):
        return self.__publication_year

    @publication_year.setter
    def publication_year(self, value):
        year = int(value)
        if year >= 0 and year < 3000:
            self.__publication_year = value

    def __str__(self):
        return f"Book name: {self.name}\n" \
                f"Author: {self.author}\n" \
                f"ISBN: {self.ISBN}\n" \
                f"Publication year: {self.publication_year}"
