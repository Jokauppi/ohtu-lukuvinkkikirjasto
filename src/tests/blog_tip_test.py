import unittest
from entities.blog_tip import BlogTip


class TestBlogTip(unittest.TestCase):
    def setUp(self):
        self.blogtip = BlogTip("name", "author", "www.blog1.com")

    def test_getName(self):
        self.assertEqual(self.blogtip.name, "name")

    def test_getAuthor(self):
        self.assertEqual(self.blogtip.author, "author")
    
    def test_getUrl(self):
        self.assertEqual(self.blogtip.url, "www.blog1.com")

    def test_changeName(self):
        self.blogtip.name = "newName of blog version 2.2"
        self.assertEqual(self.blogtip.name, "newName of blog version 2.2")

    def test_changeAuthor(self):
        self.blogtip.author = "Firstname, M. Lastname & Otherguy McDonald"
        self.assertEqual(self.blogtip.author, "Firstname, M. Lastname & Otherguy McDonald")
    
    def test_changeUrl(self):
        self.blogtip.url = "www.change.com"
        self.assertEqual(self.blogtip.url, "www.change.com")
    
    def test_name_is_null(self):
         self.assertRaises(
            ValueError,
            lambda: BlogTip("", "author", "www.blog1.com")
        )
    
    def test_name_is_not_string(self):
        self.assertRaises(
            TypeError,
            lambda: BlogTip(int(111), "author", "www.blog1.com")
        )
    
    def test_author_is_null(self):
         self.assertRaises(
            ValueError,
            lambda: BlogTip("name", "", "www.blog1.com")
        )
    
    def test_author_is_not_string(self):
        self.assertRaises(
            TypeError,
            lambda: BlogTip("name", int(111), "www.blog1.com")
        )
    
    def test_url_is_null(self):
         self.assertRaises(
            ValueError,
            lambda: BlogTip("name", "author", "")
        )
    
    def test_blog_tip_not_equals_other_blogtip(self):
         self.assertFalse(self.blogtip == BlogTip('name3', 'author3', 'www.123.com'))
    
    def test_blog_tip_equals_other_blogtip(self):
         self.assertTrue(self.blogtip == BlogTip("name", "author", "www.blog1.com"))
    
    def test_blog_tip_isInstance(self):
         self.assertTrue(self.blogtip.__eq__(self.blogtip))
    
    def test_blog_tip_isNotInstance(self):
         self.assertFalse(self.blogtip == int(111))
