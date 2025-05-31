def multiply(a, b):
    return a * b

import unittest

class Testmultiply(unittest.TestCase):
    
    def test_multiply(self):
        self.assertEqual(multiply(6,9),54)
        self.assertNotEqual(multiply(5,8),45)
        
if  __name__ == '__main__':
    unittest.main()
    