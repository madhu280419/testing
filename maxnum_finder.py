import unittest

def findmax(num):
    return max(num)

class TestFindMax(unittest.TestCase):
    def testmax(self):
        self.assertEqual(max([1,3,5,9,6,8,7,4]),9)
        
if __name__ == '__main__':
    unittest.main()               