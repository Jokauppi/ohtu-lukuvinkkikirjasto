import unittest
from repositories.book_tip_repository import BookTipRepository
from entities.book_tip import BookTip



class TestBookTipRepository(unittest.TestCase):
    def setUp(self):
        #repository.delete_all()

        self.repository = BookTipRepository()

        self.booktip_a = BookTip('Book1', 'Firstname1, lastname1', '1234', '2001')
        self.booktip_b = BookTip('Book2', 'Firstname2, lastname2', '1234', '2002')

    def test_add(self):
        self.repository.add(self.booktip_a)
        booktips = self.repository.get_all()

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())

    def test_get_all(self):
        self.repository.add(self.booktip_a)
        self.repository.add(self.booktip_b)
        booktips = self.repository.get_all()

        self.assertEqual(len(booktips), 2)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), self.booktip_b.__str__())
