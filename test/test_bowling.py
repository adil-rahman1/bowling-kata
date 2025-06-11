import unittest
from bowling import calculate_bowling_score

class TestBowlingScore(unittest.TestCase):
    def test_strike(self):
        result = calculate_bowling_score("X")
        self.assertEqual(result, 10)
