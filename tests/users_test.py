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
        pass

    def testValidEmailInvalidPassword(self):
        pass

    def testInvalidEmailInvalidPassword(self):
        pass

if __name__ == '__main__':
    unittest.main()
