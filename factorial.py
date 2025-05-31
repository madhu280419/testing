import unittest
def factorial(n):
    if n < 0:
        raise ValueError("factorial is not defined by negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


class TestFactorial(unittest.TestCase):
    
    def testfactorialbase(self):
        self.assertEqual(factorial(1),1)
        
    def testfactorial_positive(self):
        self.assertEqual(factorial(6),720)
        self.assertNotEqual(factorial(7),879)
        
    def testfactorial_negative(self):
        #self.assertEqual(factorial(6),720)
        with self.assertRaises(ValueError):    # Should raise ValueError for negative numbers
            factorial(-6)
        
if  __name__ == '__main__':
    unittest.main()
        
    