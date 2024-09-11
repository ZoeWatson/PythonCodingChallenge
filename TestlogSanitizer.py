import unittest
import logSanitizer
from unittest.mock import patch

# This File is AI generated from ChatGPT with minor modifications and additions
class TestGenerateIndexArray(unittest.TestCase):

    def test_empty_stage_array(self):
        stage_array = []
        self.assertEqual(logSanitizer.generate_index_array(stage_array), [])

    def test_single_stage(self):
        stage_array = [1]
        self.assertEqual(logSanitizer.generate_index_array(stage_array), [0])

    def test_multiple_same_stages(self):
        stage_array = [1, 1, 1, 1]
        self.assertEqual(logSanitizer.generate_index_array(stage_array), [0])

    def test_multiple_different_stages(self):
        stage_array = [0, 1, 2, 3]
        self.assertEqual(logSanitizer.generate_index_array(stage_array), [0, 1, 2, 3])

    def test_negative_stages(self):
        stage_array = [-1, -2, -3, -4]
        self.assertEqual(logSanitizer.generate_index_array(stage_array), [])

    def test_invalid_stages(self):
        stage_array = [10, 22, 4, -5]
        self.assertEqual(logSanitizer.generate_index_array(stage_array), [])

    def test_negative_stages(self):
        stage_array = [-1, -2, -3, -4]
        self.assertEqual(logSanitizer.generate_index_array(stage_array), [])

    def test_mixed_stages(self):
        stage_array = [1, 2, 2, 3, 3, 0]
        self.assertEqual(logSanitizer.generate_index_array(stage_array), [0, 1, 3, 5])

    def test_non_integer_data(self):
        stage_array = [1, 2, 'a', 3]
        self.assertEqual(logSanitizer.generate_index_array(stage_array), [0, 1, 3])

if __name__ == '__main__':
    unittest.main()