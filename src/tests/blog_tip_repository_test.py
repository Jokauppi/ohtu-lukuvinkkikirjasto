import sqlite3
from typing import Any
import unittest
from repositories.blog_tip_repository import BlogTipRepository
from entities.blog_tip import BlogTip


class TestBlogTipRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.repository = BlogTipRepository(self.connection)

        self.tip_a = BlogTip('Blog1', 'Blogaaja1', 'blog.example.com/1', 1, False) 
        self.tip_b = BlogTip('Blog2', 'Blogaaja2', 'blog.example.com/2', 2, False)
        self.tip_c = BlogTip('Blog3', 'Blogaaja3', 'blog.example.com/3', 3, True) 
        self.tip_d = BlogTip('Blog4', 'Blogaaja4', 'blog.example.com/4', 4, True)

    def test_add(self):
        self.repository.add(self.tip_a)
        tips = self.repository.get_all()

        self.assertEqual(len(tips), 1)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())

    def test_get_all(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        tips = self.repository.get_all()

        self.assertEqual(len(tips), 2)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())
        self.assertEqual(tips[1].__str__(), self.tip_b.__str__())

    def test_get_read(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        self.repository.add(self.tip_c)
        self.repository.add(self.tip_d)
        tips = self.repository.get_read(True)

        self.assertEqual(len(tips), 2)
        self.assertEqual(tips[0].__str__(), self.tip_c.__str__())
        self.assertEqual(tips[1].__str__(), self.tip_d.__str__())
    
    def test_get_unread(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        self.repository.add(self.tip_c)
        self.repository.add(self.tip_d)
        tips = self.repository.get_read(False)

        self.assertEqual(len(tips), 2)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())
        self.assertEqual(tips[1].__str__(), self.tip_b.__str__())
    
    def test_marking_as_read_works_correctly(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        tips = self.repository.get_read(True)

        self.assertEqual(len(tips), 0)

        self.repository.mark_as_read("1")
        tips = self.repository.get_read(True)

        self.assertEqual(len(tips), 1)
        self.assertEqual(tips[0].__str__(), "Index:  1\nRead:   True\nTitle:  Blog1\nAuthor: Blogaaja1\nurl:    blog.example.com/1\n")

    def test_cannot_add_same_blog_twice(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_a)
        tips = self.repository.get_all()

        self.assertEqual(len(tips), 1)
    
    def test_delete_all(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        self.repository.delete_all()
        
        tips = self.repository.get_all()
        self.assertEqual(len(tips), 0)
    
    def test_drop_tables(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        self.repository.drop_tables()
        self.assertRaises(
            Exception,
            lambda: self.repository.get_all()
        )
