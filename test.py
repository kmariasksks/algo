import unittest

from main import min_speed

class TestMinEatingSpeed(unittest.TestCase):
    
    def test_example1(self):
        piles = [3, 6, 7, 11]
        H = 8
        result = min_speed(piles, H)
        self.assertEqual(result, 4)

    def test_example2(self):
        piles = [30, 11, 23, 4, 20]
        H = 5
        result = min_speed(piles, H)
        self.assertEqual(result, 30)

    def test_example3(self):
        piles = [30, 11, 23, 4, 20]
        H = 6
        result = min_speed(piles, H)
        self.assertEqual(result, 23)

if __name__ == '__main__':
    unittest.main()