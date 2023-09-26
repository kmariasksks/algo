import unittest

from main import find_largest_k

class TestFindLargestK(unittest.TestCase):
    def test_1(self):
        numbers = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        result = find_largest_k(numbers, k)
        expected_result = (22, 2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
    