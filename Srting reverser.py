import unittest

def reversestring(s):
    return s[::-1]


class Testreversestring(unittest.TestCase):
    def testreverse_string(self):
        self.assertEqual(reversestring("madhu"),"uhdam")
        self.assertNotEqual(reversestring("madhu"),"madhu")
        
        
if __name__ == '__main__':
    unittest.main()