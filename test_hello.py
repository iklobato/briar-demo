import unittest

from hello import bow, greet


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class BowTest(unittest.TestCase):
    def test_returns_bow(self):
        self.assertEqual(bow(), "bow")


if __name__ == "__main__":
    unittest.main()
