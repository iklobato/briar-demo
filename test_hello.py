import unittest

from hello import greet, wave


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class WaveTest(unittest.TestCase):
    def test_returns_wave(self):
        self.assertEqual(wave(), "wave")


if __name__ == "__main__":
    unittest.main()
