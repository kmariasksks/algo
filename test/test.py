import unittest
import sys
import os

sys.path.append(os.path.abspath('D:/algo/src'))

from main import naive_search_last_occurrence

class TestNaiveSearchLastOccurrence(unittest.TestCase):
    def test_last_occurrence_found(self):
        haystack = "abracadabra"
        needle = "abra"
        result, comparisons = naive_search_last_occurrence(haystack, needle)
        self.assertEqual(result, 7)
        self.assertGreater(comparisons, 0)

    def test_last_occurrence_not_found(self):
        haystack = "abracadabra"
        needle = "xyz"
        result, comparisons = naive_search_last_occurrence(haystack, needle)
        self.assertEqual(result, -1)
        self.assertGreater(comparisons, 0)

    def test_empty_needle(self):
        haystack = "abracadabra"
        needle = ""
        result, comparisons = naive_search_last_occurrence(haystack, needle)
        self.assertEqual(result, len(haystack) - 1)
        self.assertEqual(comparisons, 0)


if __name__ == '__main__':
    unittest.main()
