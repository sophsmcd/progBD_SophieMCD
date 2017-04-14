
from calculator import *

import unittest
from math import sin 
from math import cos
from math import log

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

        def testsin(self):
            self.assertEqual(sin(5), -0.9589242746631385)
            self.assertEqual(sin(10), -0.5440211108893698)
            self.assertEqual(sin(15), 0.6502878401571168)
            self.assertEqual(sin(30), -0.9880316240928618)
        def testcos(self):
            self.assertEqual(cos(5), 0.28366218546322625)
            self.assertEqual(cos(10), -0.8390715290764524)
            self.assertEqual(cos(15), -0.7596879128588213)
            self.assertEqual(cos(30), 0.15425144988758405)
        
        def testlog(self):
            self.assertEqual(log(5), 1.6094379124341003)
            self.assertEqual(log(10), 2.302585092994046)
            self.assertEqual(log(15), 2.70805020110221)
            self.assertEqual(log(30), 3.4011973816621555)
                
            
if __name__ == '__main__':
    unittest.main()