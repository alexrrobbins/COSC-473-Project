import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from backend.user import User
from backend.admin import Admin
import unittest2 as unittest

class Users_Test(unittest.TestCase):
    def testSuccessfulRegister(self):
        pass

    def testUnsuccessfulRegister(self):
        pass

    def testSuccessfulLogin(self):
        test_user = User('testsheep@gmail.com','1729983526')
        result = test_user.verify_credentials()
        self.assertEqual(result, True)

    def testInvalidEmailValidPassword(self):
        test_user = User('testsheep3@gmail.com','1729983526')
        result = test_user.verify_credentials()
        self.assertEqual(result,False)

    def testValidEmailInvalidPassword(self):
        test_user = User('testsheep@gmail.com','567340989')
        result = test_user.verify_credentials()
        self.assertEqual(result,False)

    def testInvalidEmailInvalidPassword(self):
        test_user = User('testsheep1@gmail.com','567340989')
        result = test_user.verify_credentials()
        self.assertEqual(result,False)

if __name__ == '__main__':
    unittest.main()
