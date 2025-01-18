import unittest

class TestSampleSetup(unittest.TestCase):
    def test_execute_successfully(self):
        """Test to check if 1 equals 1"""
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
