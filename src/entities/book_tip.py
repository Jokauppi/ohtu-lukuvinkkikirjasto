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
            raise TypeError("Name should be string type")
        if len(value) <= 0 or len(value) > 100:
            raise ValueError("Name length should be between 1 and 100 characters")
        self.__name = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Name should be string type")
        if len(value) <= 0 or len(value) > 100:
            raise ValueError("Name length should be between 1 and 100 characters")
        self.__author = value

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str):
            raise TypeError("ISBN should be string type")
        if len(value) <= 0 and len(value) > 20:
            raise ValueError("ISBN length should be between 1 and 20 characters long")
        self.__isbn = value

    @property
    def publication_year(self):
        return self.__publication_year

    @publication_year.setter
    def publication_year(self, value):
        if not isinstance(value, str):
            raise TypeError("Year should be string type")
        year = int(value)
        if year < 0 or  year > 3000:
            raise ValueError("Year should be between 0 and 3000")
        self.__publication_year = value

    def __str__(self):
        return f"Book name: {self.name}\n" \
                f"Author: {self.author}\n" \
                f"isbn: {self.isbn}\n" \
                f"Publication year: {self.publication_year}"
