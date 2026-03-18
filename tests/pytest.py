import unittest
from logic_utils import get_range_for_difficulty, update_score, check_guess


class TestGameLogic(unittest.TestCase):
    
    def test_get_range_for_difficulty(self):
        # Test Bug #1: get_range_for_difficulty
        self.assertEqual(get_range_for_difficulty('Easy'), (1, 20), "Error: Easy range is incorrect")
        self.assertEqual(get_range_for_difficulty('Normal'), (1, 100), "Error: Normal range is incorrect")
        self.assertEqual(get_range_for_difficulty('Hard'), (1, 50), "Error: Hard range is incorrect")

    def test_update_score(self):
        # Test Bug #3: update_score with "Too High"
        self.assertEqual(update_score(100, "Too High", 1), 95, "Error: Score did not penalize for even attempt")
        self.assertEqual(update_score(100, "Too High", 2), 95, "Error: Score did not penalize for odd attempt")

    def test_check_guess(self):
        # Existing check_guess tests (you can add more based on actual implementation)
        self.assertTrue(check_guess(50, 50), "Error: Guess should be correct")
        self.assertFalse(check_guess(40, 50), "Error: Guess should be incorrect")


if __name__ == '__main__':
    unittest.main()