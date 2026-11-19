import unittest

from hello import cheer, greet


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class CheerTest(unittest.TestCase):
    def test_cheers(self):
        self.assertEqual(cheer(), "Hooray!")


if __name__ == "__main__":
    unittest.main()
