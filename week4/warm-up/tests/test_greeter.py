import unittest
from src.greeter import greeter as greetTest

class TestGreeter(unittest.TestCase):
    def test_greeter(self):
        self.assertEqual(greetTest('Thyme'), 'Hello Thyme')

if __name__ == '__main__':
    unittest.main()