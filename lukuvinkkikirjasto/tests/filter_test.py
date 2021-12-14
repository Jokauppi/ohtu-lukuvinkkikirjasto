import unittest
from entities.filter import Filter


class TestFilter(unittest.TestCase):
    def setUp(self):
        self.filter = Filter()
        self.filter.types = ["book"]
        self.filter.name = "Book1"
        self.filter.author = "Author1"
        self.filter.isbn = "111111"
        self.filter.publication_year = "2001"
        self.filter.url = "www.Book1.com"
        self.filter.read = "k"
        self.filter.comment = "This is a comment"
        self.filter.taglist = "Tag1"
        self.filter.taglist = "Tag2"

    def test_attributes(self):
        self.assertEqual(len(self.filter.types), 1)
        self.assertEqual(self.filter.types[0], "book")
        self.assertEqual(self.filter.name, "Book1")
        self.assertEqual(self.filter.author, "Author1")
        self.assertEqual(self.filter.isbn, "111111")
        self.assertEqual(self.filter.publication_year, "2001")
        self.assertEqual(self.filter.url, "www.Book1.com")
        self.assertEqual(self.filter.read, "k")
        self.assertEqual(self.filter.comment, "This is a comment")
        self.assertEqual(len(self.filter.taglist), 2)
        self.assertEqual(self.filter.taglist[0], "Tag1")
        self.assertEqual(self.filter.taglist[1], "Tag2")
    
    def test_clear_filters(self):
        self.filter.clear_filters()
        self.assertEqual(len(self.filter.types), 0)
        self.assertFalse(self.filter.name)
        self.assertFalse(self.filter.author)
        self.assertFalse(self.filter.isbn)
        self.assertFalse(self.filter.publication_year)
        self.assertFalse(self.filter.url)
        self.assertFalse(self.filter.read)
        self.assertFalse(self.filter.comment)
        self.assertEqual(len(self.filter.taglist), 0)
    
    def test_book_filters(self):
        self.filter.name=''
        f, v, c, sv, so = self.filter.book_filters()

        self.assertEqual(len(f), 7)
        self.assertEqual(len(v), 7)
        self.assertEqual(len(c), 7)
        self.assertEqual(len(sv), 2)
        self.assertEqual(len(so), 2)
        self.filter.clear_filters()
        self.filter.name='Book1'
        self.filter.read = "e"
        f, v, c, sv, so = self.filter.book_filters()
        self.assertEqual(len(f), 2)
        self.assertEqual(len(v), 2)
        self.assertEqual(len(c), 2)
        self.assertEqual(len(sv), 1)
        self.assertEqual(len(so), 1)
    
    def test_blog_filters(self):
        self.filter.name=''
        f, v, c, sv, so = self.filter.blog_filters()

        self.assertEqual(len(f), 6)
        self.assertEqual(len(v), 6)
        self.assertEqual(len(c), 6)
        self.assertEqual(len(sv), 2)
        self.assertEqual(len(so), 2)
        self.filter.clear_filters()
        self.filter.name='Book1'
        self.filter.read = "e"
        f, v, c, sv, so = self.filter.blog_filters()
        self.assertEqual(len(f), 2)
        self.assertEqual(len(v), 2)
        self.assertEqual(len(c), 2)
        self.assertEqual(len(sv), 1)
        self.assertEqual(len(so), 1)
    
    def test_video_filters(self):
        self.filter.name=''
        f, v, c, sv, so = self.filter.video_filters()

        self.assertEqual(len(f), 5)
        self.assertEqual(len(v), 5)
        self.assertEqual(len(c), 5)
        self.assertEqual(len(sv), 1)
        self.assertEqual(len(so), 1)
        self.filter.clear_filters()
        self.filter.name='Book1'
        self.filter.read = "e"
        f, v, c, sv, so = self.filter.video_filters()
        self.assertEqual(len(f), 2)
        self.assertEqual(len(v), 2)
        self.assertEqual(len(c), 2)
        self.assertEqual(len(sv), 1)
        self.assertEqual(len(so), 1)
    
    def test_field_and_value(self):
        self.filter.clear_filters()
        self.filter.add_field_and_value([], [], [], '', '')
        f, v, c, sv, so = self.filter.book_filters()
        self.assertEqual(len(f), 0)
    
    def test_sortby(self):
        self.filter.clear_filters()
        self.filter.add_sort_bys([], [], '', '')
        f, v, c, sv, so = self.filter.book_filters()
        self.assertEqual(len(sv), 0)
