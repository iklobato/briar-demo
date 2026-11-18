import unittest

from hello import greet, murmur


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class MurmurTest(unittest.TestCase):
    def test_murmurs_in_lower_case(self):
        self.assertEqual(murmur("Ana"), "hello, ana!")


if __name__ == "__main__":
    unittest.main()
