import unittest

from hello import greet, whisper


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class WhisperTest(unittest.TestCase):
    def test_whispers_a_name(self):
        self.assertEqual(whisper("Ana"), "hello, ana!")

    def test_whispers_without_a_name(self):
        self.assertEqual(whisper(), "hello, none!")


if __name__ == "__main__":
    unittest.main()
