import unittest
from entities.book_tip import BookTip
from service import Service

class MockBookTipRepository:
    def __init__(self, booktips=None):
        self.booktips = booktips or []

    def get_all(self):
        return self.booktips

    

    def add(self, booktip):
        self.booktips.append(booktip)

        return booktip

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service(MockBookTipRepository())

        self.booktip_a = BookTip('Book1', 'Firstname1, lastname1', '1234', '2001')
        self.booktip_b = BookTip('Book2', 'Firstname2, lastname2', '1234', '2002')
    
    def test_add_book_tip(self):

        self.service.create_book_tip('Book1', 'Firstname1, lastname1', '1234', '2001')
        booktips = self.service.get_all_book_tips()

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
