import unittest

from hello import greet, hush


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class HushTest(unittest.TestCase):
    def test_hushes_a_name(self):
        self.assertEqual(hush("Ana"), "hello, ana")


if __name__ == "__main__":
    unittest.main()
