import unittest

def palindrome(s):
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(palindrome("tenet"))
        
    def test_palindrome_false(self):
        self.assertFalse(palindrome("madhu"))
        
if __name__ == '__main__':
    unittest.main()