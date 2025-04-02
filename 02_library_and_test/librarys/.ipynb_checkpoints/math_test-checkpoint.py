import unittest
from librarys.math import add

class TestAdd(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(add(1,2), 3)

    def test_negative(self):
        self.assertEqual(add(-1,-2), -3)


if __name__ == '__main__':
    unittest.main()