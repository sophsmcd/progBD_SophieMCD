
from calculator import *
import unittest

class MyTest(unittest.TestCase): 
        def testSum1(self):
            self.assertEqual(sum(2,2), 4)
            self.assertEqual(sum(5,3), 8)
            self.assertEqual(sum(4,0), 4)
    
        def testsubtract(self): 
            self.assertEqual(subtract(2,2), 0)
            self.assertEqual(subtract(5,3), 2)
            self.assertEqual(subtract(4,0), 4)
            self.assertEqual(subtract(3,4), -1)

        def testmultiply(self): 
            self.assertEqual(multiply(2,2), 4)
            self.assertEqual(multiply(5,3), 15)
            self.assertEqual(multiply(4,0), 0)
            self.assertEqual(multiply(3,4), 12)
            
        def testdivide(self):
            self.assertEqual(divide(2,2), 1)
            self.assertEqual(divide(15,5), 3)
            self.assertEqual(divide(4, 2), 2)
            self.assertEqual(divide(12, 2), 6)
        
        def testexponent(self): 
            self.assertEqual(exponent(2,3),8)
            self.assertEqual(exponent(1,2), 1)
            self.assertEqual(exponent(4,3), 64)
            self.assertEqual(exponent(3,3), 27)
            
        def testsquare(self):
            self.assertEqual(square(2), 4)
            self.assertEqual(square(3), 9)
            self.assertEqual(square(4), 16)
            self.assertEqual(square(5), 25)
        
        def testsqrt(self):
            self.assertEqual(sqrt(16), 4)
            self.assertEqual(sqrt(25), 5)
            self.assertEqual(sqrt(9), 3)
            self.assertEqual(sqrt(4), 2)
            
        def testremainders(self):
            self.assertequal(remainders([2,5,4,6,7],2,4,6)
            self.assertequal(remainders([3,6,8,9,10],6,8,10)
            self.assertequal(remainders([10,11,12,13],10,12)
            
if __name__ == '__main__':
    unittest.main()
    