import unittest

from hello import greet, murmur2


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class Murmur2Test(unittest.TestCase):
    def test_returns_psst(self):
        self.assertEqual(murmur2(), "psst")


if __name__ == "__main__":
    unittest.main()
