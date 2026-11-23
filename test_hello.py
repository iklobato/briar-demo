import unittest

from hello import greet, nod


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class NodTest(unittest.TestCase):
    def test_nods_to_a_name(self):
        self.assertEqual(nod("Ana"), "Yes, Ana.")


if __name__ == "__main__":
    unittest.main()
