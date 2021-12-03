from entities.book_tip import BookTip


class Service:
    def __init__(self, repository):
        self._repository = repository

    def create_book_tip(self, name, author, isbn, publication_year):
        book_tip = BookTip(name, author, isbn, publication_year)
        return self._repository.add(book_tip)

    def get_all_book_tips(self):
        return self._repository.get_all()

    def mark_book_tip_as_read(self, id_number):
        return self._repository.mark_as_read(id_number)
    
    def search_tips(self, fields, values, comparators, sortByValues, sortbyOrders):
        return self._repository.search_tips(fields, values, comparators, sortByValues, sortbyOrders)