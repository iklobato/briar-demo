import unittest

from hello import greet, shout


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class ShoutTest(unittest.TestCase):
    def test_shouts_a_name(self):
        self.assertEqual(shout("Ana"), "HELLO, ANA!")

    def test_shouts_without_a_name(self):
        self.assertEqual(shout(), "HELLO, NONE!")


if __name__ == "__main__":
    unittest.main()
