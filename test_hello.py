import unittest

from hello import greet, whisper


class GreetTest(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")


class WhisperTest(unittest.TestCase):
    def test_whisper(self):
        self.assertEqual(whisper("Hi"), "hi...")


if __name__ == "__main__":
    unittest.main()
