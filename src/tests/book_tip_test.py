import unittest
from entities.book_tip import BookTip


class TestBookTip(unittest.TestCase):
    def setUp(self):
        self.booktip = BookTip("name", "author", "9781107009462", "2021")

    def test_getName(self):
        self.assertEqual(self.booktip.name, "name")

    def test_getAuthor(self):
        self.assertEqual(self.booktip.author, "author")
    
    def test_getISBN(self):
        self.assertEqual(self.booktip.isbn, "9781107009462")
    
    def test_getPublicationYear(self):
        self.assertEqual(self.booktip.publication_year, "2021")
