import sqlite3
from typing import Any
import unittest
from repositories.book_tip_repository import BookTipRepository
from entities.book_tip import BookTip


class TestBookTipRepository(unittest.TestCase):
    def setUp(self):
        #book_tip_repository.delete_all()
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.book_tip_repository = BookTipRepository(self.connection)

        self.booktip_a = BookTip('Book1', 'Firstname1, lastname1', '123-456', '2001', 1, False) 
        self.booktip_b = BookTip('Book2', 'Firstname2, lastname2', '132-456', '2002', 2, False)

    def test_add(self):
        self.book_tip_repository.add(self.booktip_a)
        booktips = self.book_tip_repository.get_all()

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())

    def test_get_all(self):
        self.book_tip_repository.add(self.booktip_a)
        self.book_tip_repository.add(self.booktip_b)
        booktips = self.book_tip_repository.get_all()

        self.assertEqual(len(booktips), 2)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), self.booktip_b.__str__())

    def test_cannot_add_same_book_twice(self):
        self.book_tip_repository.add(self.booktip_a)
        self.book_tip_repository.add(self.booktip_a)
        booktips = self.book_tip_repository.get_all()

        self.assertEqual(len(booktips), 1)
    
    def test_delete_all(self):
        self.book_tip_repository.add(self.booktip_a)
        self.book_tip_repository.add(self.booktip_b)
        self.book_tip_repository.delete_all()
        
        booktips = self.book_tip_repository.get_all()
        self.assertEqual(len(booktips), 0)
    
    def test_drop_tables(self):
        self.book_tip_repository.add(self.booktip_a)
        self.book_tip_repository.add(self.booktip_b)
        self.book_tip_repository.drop_tables()
        self.assertRaises(
            Exception,
            lambda: self.book_tip_repository.get_all()
        )
    
    def test_search_book_tips(self):
        self.book_tip_repository.add(self.booktip_a)
        self.book_tip_repository.add(self.booktip_b)
        booktip_c = BookTip('Book1', 'Firstname1, lastname1', '2222222', '2002', 1, False)
        self.book_tip_repository.add(booktip_c)
        booktips = self.book_tip_repository.search_tips([], [], [], [], [])
        self.assertEqual(len(booktips), 3)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), self.booktip_b.__str__())
        self.assertEqual(booktips[2].__str__(), booktip_c.__str__())
        booktips = self.book_tip_repository.search_tips(['name'], ['book1'], [], [], [])
        self.assertEqual(len(booktips), 2)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), booktip_c.__str__())
        booktips = self.book_tip_repository.search_tips(['name', 'author'], ['book1', 'Firstname1, lastname1'], [], ['name', 'author'], ['ASC','DESC'])
        self.assertEqual(len(booktips), 2)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), booktip_c.__str__())
        booktips = self.book_tip_repository.search_tips([], [], [], ['name', 'author'], ['ASC','DESC'])
        self.assertEqual(len(booktips), 3)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), self.booktip_b.__str__())
        self.assertEqual(booktips[2].__str__(), booktip_c.__str__())
        self.assertEqual(self.book_tip_repository.where_string([],[]), "")
        self.assertEqual(self.book_tip_repository.order_string([],[]), "")