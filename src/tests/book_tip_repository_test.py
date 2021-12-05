import sqlite3
from typing import Any
import unittest
from repositories.book_tip_repository import BookTipRepository
from entities.book_tip import BookTip


class TestBookTipRepository(unittest.TestCase):
    def setUp(self):
        #repository.delete_all()
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.repository = BookTipRepository(self.connection)

        self.tip_a = BookTip('Book1', 'Firstname1, lastname1', '123-456', '2001', 1, False) 
        self.tip_b = BookTip('Book2', 'Firstname2, lastname2', '132-456', '2002', 2, False)
        self.tip_c = BookTip('Book3', 'Firstname3, lastname3', '123-987', '2003', 3, True)
        self.tip_d = BookTip('Book4', 'Firstname4, lastname4', '123-983', '2004', 4, True)

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
        self.assertEqual(tips[0].__str__(), "Title:  Book1\nAuthor: Firstname1, lastname1\nISBN:   123-456\nYear:   2001\n")

    def test_cannot_add_same_book_twice(self):
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
