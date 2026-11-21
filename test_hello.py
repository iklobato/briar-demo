import unittest

from hello import greet, shout


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class ShoutTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")


if __name__ == "__main__":
    unittest.main()
