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

    def test_changeName(self):
        self.booktip.name = "newName of nook version 2.2"
        self.assertEqual(self.booktip.name, "newName of nook version 2.2")

    def test_changeAuthor(self):
        self.booktip.author = "Firstname, M. Lastname & Otherguy McDonald"
        self.assertEqual(self.booktip.author, "Firstname, M. Lastname & Otherguy McDonald")
    
    def test_changeISBN(self):
        self.booktip.isbn = "11111-241548"
        self.assertEqual(self.booktip.isbn, "11111-241548")
    
    def test_changePublicationYear(self):
        self.booktip.publication_year = "2022"
        self.assertEqual(self.booktip.publication_year, "2022")
    
    def test_str(self):
        self.assertEqual(self.booktip.__str__(), 'Title:  name\nAuthor: author\nISBN:   9781107009462\nYear:   2021\n')
    
    def test_name_is_null(self):
         self.assertRaises(
            ValueError,
            lambda: BookTip("", "author", "9781107009462", "2021")
        )
    
    def test_name_is_not_string(self):
        self.assertRaises(
            TypeError,
            lambda: BookTip(int(111), "author", "9781107009462", "2021")
        )
    
    def test_author_is_null(self):
         self.assertRaises(
            ValueError,
            lambda: BookTip("name", "", "9781107009462", "2021")
        )
    
    def test_author_is_not_string(self):
        self.assertRaises(
            TypeError,
            lambda: BookTip("name", int(111), "9781107009462", "2021")
        )
    
    def test_isbn_is_null(self):
         self.assertRaises(
            ValueError,
            lambda: BookTip("name", "author", "", "2021")
        )
    
    def test_isbn_is_not_string(self):
        self.assertRaises(
            TypeError,
            lambda: BookTip("name", "author", int(111), "2021")
        )
    
    def test_isbn_contains_wrong_characters(self):
         self.assertRaises(
            ValueError,
            lambda: BookTip("name", "author", "11A1", "2021")
        )

    def test_publication_year_non_numeric(self):
         self.assertRaises(
            ValueError,
            lambda: BookTip("name", "author", "2000", "20A2")
        )
    
    def test_publication_year_is_not_string(self):
        self.assertRaises(
            TypeError,
            lambda: BookTip("name", "author", "2000" , int(111))
        )
    
    def test_publication_year_not_in_range(self):
         self.assertRaises(
            ValueError,
            lambda: BookTip("name", "author", "1111", "1000000")
        )
    
    def test_book_tip_not_equals_other_booktip(self):
         self.assertFalse(self.booktip == BookTip('name3', 'author3', '888', '1999'))
    
    def test_book_tip_equals_other_booktip(self):
         self.assertTrue(self.booktip == BookTip("name", "author", "9781107009462", "2021"))
    
    def test_book_tip_isInstance(self):
         self.assertTrue(self.booktip.__eq__(self.booktip))
    
    def test_book_tip_isNotInstance(self):
         self.assertFalse(self.booktip == int(111))