import unittest

from hello import greet, hush


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class HushTest(unittest.TestCase):
    def test_returns_shh(self):
        self.assertEqual(hush(), "shh")


if __name__ == "__main__":
    unittest.main()
