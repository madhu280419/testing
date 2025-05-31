import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(7, 3), 10)
        self.assertNotEqual(add(7,3),11)
       

    def test_add_negative(self):
        self.assertEqual(add(-3, -9), -12)
        
if __name__ == '__main__':
    unittest.main()
