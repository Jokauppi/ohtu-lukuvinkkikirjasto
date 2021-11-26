class BookTip:
    def __init__(self, name, author, ISBN, publication_year):
        self._name = name
        self._author = author
        self._ISBN = ISBN
        self._publication_year = publication_year

    def getName(self):
        return self._name

    def getAuthor(self):
        return self._author

    def getISBN(self):
        return self._ISBN

    def getPublicationYear(self):
        return self._publication_year
