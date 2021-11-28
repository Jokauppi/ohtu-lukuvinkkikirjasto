import unittest
from repositories.book_tip_repository import book_tip_repository
from entities.book_tip import BookTip



class TestBookTipRepository(unittest.TestCase):
    def setUp(self):
        #book_tip_repository.delete_all()


        self.booktip_a = BookTip('Book1', 'Firstname1, lastname1', '1234', '2001')
        self.booktip_b = BookTip('Book2', 'Firstname2, lastname2', '1234', '2002')

    def test_add(self):
        book_tip_repository.add(self.booktip_a)
        booktips = book_tip_repository.get_all()

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())

    def test_get_all(self):
        book_tip_repository.add(self.booktip_a)
        book_tip_repository.add(self.booktip_b)
        booktips = book_tip_repository.get_all()

        self.assertEqual(len(booktips), 2)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), self.booktip_b.__str__())