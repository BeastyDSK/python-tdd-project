import unittest
from src.main import add

class TestUnexceptedInput(unittest.TestCase):
    def test_empty_input(self):
        """Should return zero when the input is empty or is not defined"""
        self.assertEqual(add(""), 0)
        self.assertEqual(add(None), 0)

    def test_non_string_input(self):
        """Should return zero when the input is not a string"""
        self.assertEqual(add(100), 0)
        self.assertEqual(add(True), 0)
        self.assertEqual(add({}), 0)

# To be handled
class TestExpectedInput(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
