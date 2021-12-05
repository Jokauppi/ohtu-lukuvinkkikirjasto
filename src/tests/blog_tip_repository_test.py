import sqlite3
from typing import Any
import unittest
from repositories.blog_tip_repository import BlogTipRepository
from entities.blog_tip import BlogTip


class TestBlogTipRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.blog_tip_repository = BlogTipRepository(self.connection)

        self.blogtip_a = BlogTip('Blog1','Blogaaja1', 'blog.example.com/1', 1, False) 
        self.blogtip_b = BlogTip('Blog2', 'Blogaaja2', 'blog.example.com/2', 2, False)

    def test_add(self):
        self.blog_tip_repository.add(self.blogtip_a)
        blogtips = self.blog_tip_repository.get_all()

        self.assertEqual(len(blogtips), 1)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())

    def test_get_all(self):
        self.blog_tip_repository.add(self.blogtip_a)
        self.blog_tip_repository.add(self.blogtip_b)
        blogtips = self.blog_tip_repository.get_all()

        self.assertEqual(len(blogtips), 2)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())
        self.assertEqual(blogtips[1].__str__(), self.blogtip_b.__str__())

    def test_cannot_add_same_blog_twice(self):
        self.blog_tip_repository.add(self.blogtip_a)
        self.blog_tip_repository.add(self.blogtip_a)
        blogtips = self.blog_tip_repository.get_all()

        self.assertEqual(len(blogtips), 1)
    
    def test_delete_all(self):
        self.blog_tip_repository.add(self.blogtip_a)
        self.blog_tip_repository.add(self.blogtip_b)
        self.blog_tip_repository.delete_all()
        
        blogtips = self.blog_tip_repository.get_all()
        self.assertEqual(len(blogtips), 0)
    
    def test_drop_tables(self):
        self.blog_tip_repository.add(self.blogtip_a)
        self.blog_tip_repository.add(self.blogtip_b)
        self.blog_tip_repository.drop_tables()
        self.assertRaises(
            Exception,
            lambda: self.blog_tip_repository.get_all()
        )
