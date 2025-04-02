import unittest
from librarys.converter import add_and_convert_to_string

class TestConvert(unittest.TestCase):

    def test_add(self):
        self.assertEqual(
            add_and_convert_to_string(1,2), 
            "3"
        )

    def test_type(self):
        self.assertEqual(
            type(add_and_convert_to_string(1,2)), 
            str
        )


if __name__ == '__main__':
    unittest.main()