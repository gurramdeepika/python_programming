import mathlib
import mathlib1
import unittest

class MathTest(unittest.TestCase): # class must end with test (may or may not)
    def testadd( self ): # function must start with test
        self.assertTrue(mathlib.myadd(2,3) == 5)
    def testsub( self ):
        self.assertTrue(mathlib.mysub(3,2) == 1)
    def hello( self ):
        return True
    def div( self ):
        self.assertTrue(mathlib1.mydiv(3,2) == 1.5)
    def testnotadd( self ):
        return self.assertNotEqual(mathlib.myadd(3,2),6)

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(MathTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


#main() will check for the class starts with test and
# creates an object for it then it will find for the functions ends with test and will do the unit testing

