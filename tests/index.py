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
    def test_single_number_input(self):
        """should return the first number when the input has only one number"""
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("1000"), 1000)
        self.assertEqual(add("1000,"), 1000)
        self.assertEqual(add("0"), 0)
        self.assertEqual(add("0,"), 0)
        self.assertEqual(add("-1,"), -1)
        self.assertEqual(add("+1,"), 1)
        self.assertEqual(add(","), 0)

    def test_two_number_input(self):
        """should return the sum when the input has two numbers"""
        self.assertEqual(add("1,2"), 3)
        self.assertEqual(add("1,1"), 2)
        self.assertEqual(add("0,1"), 1)
        self.assertEqual(add("0,0"), 0)
        self.assertEqual(add("-1,-1"), -2)
        self.assertEqual(add("-1,+1"), 0)
        self.assertEqual(add("+,+"), 0)

    def test_more_than_two_number_input(self):
        self.assertEqual(add("1,2,1"), 4)
        self.assertEqual(add("1,1,1290,-1290"), 2)
        self.assertEqual(add("0,1,1211"), 1212)
        self.assertEqual(add("-1,-1,2"), 0)
        self.assertEqual(add("-1,-1,+2"), 0)
        self.assertEqual(add("+,+,-"), 0)
        self.assertEqual(add("-1,-1\n+2"), 0)

    def test_new_line_delimiter(self):
        """should sucessfully calculate the sum when the input contains newline character"""
        self.assertEqual(add("1\n1"), 2)
        self.assertEqual(add("\n"), 0)
        self.assertEqual(add("1\n"), 1)
        self.assertEqual(add("1\n,"), 1)
        self.assertEqual(add("\n-1"), -1)

if __name__ == "__main__":
    unittest.main()
