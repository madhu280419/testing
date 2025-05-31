import unittest

def upper(s):
    return s.upper()
    
class testupper(unittest.TestCase):
    def testUpper(self):
        self.assertEqual(upper("madhu"),"MADHU")
        self.assertNotEqual(upper("madhu"),"madhu")
        
        
if __name__ == '__main__':
    unittest.main()