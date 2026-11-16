import unittest

import textkit


class TextkitTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(textkit.shout("hi"), "HI")

    def test_whisper(self):
        self.assertEqual(textkit.whisper("HeLLo"), "hello")


if __name__ == "__main__":
    unittest.main()
