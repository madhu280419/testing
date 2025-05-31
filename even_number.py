import unittest

def iseven(a):
    return a % 2 == 0

class Testiseven(unittest.TestCase):
    
    def test_eventrue(self):
        self.assertTrue(iseven(16))
        
    def test_evenfalse(self):
        self.assertFalse(iseven(5))
        
if  __name__ == '__main__':
    unittest.main()