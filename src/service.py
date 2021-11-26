from entities.book_tip import BookTip


class Service:
    def __init__(self, repository):
        self._repository = repository

    def create_book_tip(self, name, author, isbn, publication_year):
        book_tip = BookTip(name, author, isbn, publication_year)
        return self._repository.add(book_tip)

    def get_all_book_tips(self):
        return self._repository.get_all()
