import unittest

from hello import greet


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")

    def test_greets_world_by_default(self):
        self.assertEqual(greet(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
