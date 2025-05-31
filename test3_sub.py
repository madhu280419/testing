def subtract(a, b):
    return a-b

import unittest

class Testsubtract(unittest.TestCase):
    
    def test_subtract(self):
        self.assertEqual(subtract(8,3),5)
        self.assertnotEqual(subtract(5,3),4)
   
if  __name__ == '__main__':
    unittest.main()
    