def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

import unittest

class testdivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10,5),2)
        self.assertNotEqual(divide(3,9),29)
        
if __name__ == '__main__':
    unittest.main()
    
    
    
