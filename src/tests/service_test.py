import unittest
from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from service import Service

class MockBookTipRepository:
    def __init__(self, booktips=None):
        self.booktips = booktips or []

    def get_all(self):
        return self.booktips

    

    def add(self, booktip):
        self.booktips.append(booktip)

        return booktip

class MockBlogTipRepository:
    def __init__(self, blogips=None):
        self.blogtips = blogips or []

    def get_all(self):
        return self.blogtips

    

    def add(self, blogtip):
        self.blogtips.append(blogtip)

        return blogtip

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service(MockBookTipRepository(), MockBlogTipRepository())

        self.booktip_a = BookTip('Book1', 'Firstname1, lastname1', '1234', '2001')
        self.booktip_b = BookTip('Book2', 'Firstname2, lastname2', '1234', '2002')
        self.blogtip_a = BlogTip('Blog1', 'Firstname1, lastname1', 'www.1.com')
        self.blogtip_b = BlogTip('Blog2', 'Firstname2, lastname2', 'www.2.com')
    
    def test_add_book_tip(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year)
        booktips = self.service.get_all_book_tips()

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
    
    
    def test_get_all_book_tips(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year)
        self.service.create_book_tip(self.booktip_b.name, self.booktip_b.author, self.booktip_b.isbn, self.booktip_b.publication_year)

        booktips = self.service.get_all_book_tips()

        self.assertEqual(len(booktips), 2)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), self.booktip_b.__str__())
        
