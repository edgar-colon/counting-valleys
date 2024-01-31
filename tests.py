import unittest
from main import counting_valleys

class TestCountingValleys(unittest.TestCase):
    def test_crossing_one_valley(self):
        steps = 8
        path = "UDDDUDUU"
        result = counting_valleys(steps, path)
        self.assertEqual(result, 1)
        print("Example 1 - Crossing one valley:", result)

    def test_crossing_two_valleys(self):
        steps = 14
        path = "UDDDUDUUDDUDUU"
        result = counting_valleys(steps, path)
        self.assertEqual(result, 2)
        print("Example 2 - Crossing two valleys:", result)

    def test_crossing_three_valleys(self):
        steps = 20
        path = "UDDUDDUUUDDUUUUDDUUU"
        result = counting_valleys(steps, path)
        self.assertEqual(result, 3)
        print("Example 3 - Crossing three valleys:", result)

    def test_invalid_characters_in_path(self):
        steps = 8
        path = "UDDDUDUUA"
        with self.assertRaises(ValueError):
            counting_valleys(steps, path)

if __name__ == '__main__':
    unittest.main()
