import unittest

from hello import greet, salute


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class SaluteTest(unittest.TestCase):
    def test_salutes_a_name(self):
        self.assertEqual(salute("Ana"), "Salute, Ana!")


if __name__ == "__main__":
    unittest.main()
