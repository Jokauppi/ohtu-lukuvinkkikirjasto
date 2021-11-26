class BookTip:
    def __init__(self, name, author, ISBN, publication_year):
        self._name = name
        self._author = author
        self._ISBN = ISBN
        self._publication_year = publication_year

    def getName(self):
        return self.name

    def getAuthor(self):
        return self.author

    def getISBN(self):
        return self.ISBN

    def getPublicationYear(self):
        return self.publication_year()
