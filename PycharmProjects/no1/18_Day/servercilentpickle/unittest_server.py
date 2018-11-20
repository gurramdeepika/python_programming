import Student_Details as stutest
import unittest

class Studenttest(unittest.TestCase): # class must end with test (may or may not)

    def testadd( self ): # function must start with test
        self.assertTrue(stutest.Student('deepika',3).stu() == 'DEEPIKA')
        self.assertFalse(stutest.Student('deepika',3).stu() == 'deepika')

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Studenttest)
    unittest.TextTestRunner(verbosity=2).run(suite)
