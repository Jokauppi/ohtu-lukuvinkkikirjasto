from entities.book_tip import BookTip
from entities.blog_tip import BlogTip


class Service:
    def __init__(self, repository, blogrepository):
        self._repository = repository
        self._blogrepository = blogrepository

    def create_book_tip(self, name, author, isbn, publication_year):
        book_tip = BookTip(name, author, isbn, publication_year)
        return self._repository.add(book_tip)

    def create_blog_tip(self, name, author, url):
        blog_tip = BlogTip(name, author, url)
        return self._blogrepository.add(blog_tip)

    def get_all_book_tips(self):
        return self._repository.get_all()

    def get_all_blog_tips(self):
        return self._blogrepository.get_all()

    def mark_book_tip_as_read(self, id_number):
        return self._repository.mark_as_read(id_number)
    
    def search_tips(self, fields, values, comparators, sortByValues, sortbyOrders):
        search_result = self._repository.search_tips(fields, values, comparators, sortByValues, sortbyOrders)
        search_result += self._blogrepository.search_tips(fields, values, comparators, sortByValues, sortbyOrders)
        return search_result
    
    def search_book_tips(self, fields, values, comparators, sortByValues, sortbyOrders):
        return self._repository.search_tips(fields, values, comparators, sortByValues, sortbyOrders)
    
    def search_blog_tips(self, fields, values, comparators, sortByValues, sortbyOrders):
        return self._blogrepository.search_tips(fields, values, comparators, sortByValues, sortbyOrders)