import unittest
from src.game import generate_random_number, check_guess

class TestGame(unittest.TestCase):

    def test_generate_random_number(self):
        number = generate_random_number()
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 100)

    def test_check_guess_correct(self):
        self.assertTrue(check_guess(50, 50))

    def test_check_guess_too_high(self):
        self.assertEqual(check_guess(75, 50), "Too high!")

    def test_check_guess_too_low(self):
        self.assertEqual(check_guess(25, 50), "Too low!")

if __name__ == '__main__':
    unittest.main()