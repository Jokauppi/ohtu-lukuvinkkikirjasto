class BookTip:
    def __init__(self, name: str, author: str, ISBN: str, publication_year: str):
        self._name = name
        self._author = author
        self._ISBN = ISBN
        self._publication_year = publication_year

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def ISBN(self):
        return self._ISBN

    @property
    def publication_year(self):
        return self._publication_year

    def __str__(self):
        return f"Book name: {self._name}\n" \
                f"Author: {self._author}\n" \
                f"ISBN: {self._ISBN}\n" \
                f"Publication year: {self._publication_year}"
