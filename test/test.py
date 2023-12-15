import unittest
import os
import sys

sys.path.append(os.path.abspath('D:/algo7/src'))

from wchain import longest_chain

class TestLongestChain(unittest.TestCase):

    def test_correct_result(self):
        words = ["cat", "bat", "at", "a"]
        expected = 3
        actual = longest_chain(words)
        self.assertEqual(expected, actual)

    def test_invalid_number_of_words(self):
        words = ["c"] * 10**6
        with self.assertRaises(ValueError):
            longest_chain(words)

    def test_invalid_word_length(self):
        words = ["c" * 51]
        with self.assertRaises(ValueError):
            longest_chain(words)

    def test_invalid_word_characters(self):
        words = ["Corn"]
        with self.assertRaises(ValueError):
            longest_chain(words)

if __name__ == '__main__':
    unittest.main()