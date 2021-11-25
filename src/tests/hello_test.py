import unittest
from hello import Hello


class TestHello(unittest.TestCase):
    def setUp(self):
        self.hello = Hello()

    def test_konstruktori_luo_hello_stringin(self):
        self.assertAlmostEqual(self.hello.hello, "Hello")

