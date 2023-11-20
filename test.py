import unittest

from count_pairs import count_pairs


class TestCountOfPairsFunction(unittest.TestCase):

    def test_1(self):
        pairs = [(1, 2), (2, 4), (3, 5)]
        result = count_pairs(5, pairs)
        self.assertEqual(result, 4)

    def test_2(self):
        pairs = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
        result = count_pairs(10, pairs)
        self.assertEqual(result, 6)

    def test_3(self):
        pairs = [(2, 4), (6, 8), (10, 12), (14, 16)]
        result = count_pairs(16, pairs)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()