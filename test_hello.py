import unittest

from hello import farewell, greet


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class FarewellTest(unittest.TestCase):
    def test_says_goodbye_to_a_name(self):
        self.assertEqual(farewell("Ana"), "Goodbye, Ana!")

    def test_says_goodbye_to_world_without_a_name(self):
        self.assertEqual(farewell(), "Goodbye, world!")


if __name__ == "__main__":
    unittest.main()
