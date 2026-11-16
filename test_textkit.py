import unittest

import textkit


class TextkitTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(textkit.shout("hi"), "HI")

    def test_whisper(self):
        self.assertEqual(textkit.whisper("HeLLo"), "hello")

    def test_count_words(self):
        self.assertEqual(textkit.count_words("one two  three"), 3)

    def test_count_words_empty(self):
        self.assertEqual(textkit.count_words(""), 0)


if __name__ == "__main__":
    unittest.main()
