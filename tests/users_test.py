from flask import Flask
import flask_unittest
import flask.globals

class TestUser(flask_unittest.AppTestCase):

    def create_app(self):
        return Flask(__name__)

    def setUp(self,app):
        pass

    def tearDown(self,app):
        pass

    def testSuccessfulRegister(self,app):
        pass

    def testUnsuccessfulRegister(self,app):
        pass

    def testSuccessfulLogin(self):
        client = self.create_app().test_client()
        test_data = {'email': "testsheep@gmail.com", 'password': "1729983526"}
        response = client.post('/login_verify', data = test_data, follow_redirects=True)
        self.assertLocationHeader(response,'/welcome')

    def testInvalidEmailValidPassword(self,client):
        pass

    def testValidEmailInvalidPassword(self,client):
        pass

    def testInvalidEmailInvalidPassword(self,client):
        pass

if __name__ == '__main__':
    t = TestUser()
    t.setUp(t.create_app())
    t.testSuccessfulLogin()
