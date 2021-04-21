from flask import Flask
import flask_unittest
import flask.globals

class TestUser(flast_unittest.ClientTestCase):
    def creare_app(self):
        return Flask(__name__)

    def setUp(self,client):
        pass

    def tearDown(self,client):
        pass

    def testSuccessfulRegister(self,client):
        pass

    def testUnsuccessfulRegister(self,client):
        pass

    def testSuccessfulLogin(self,client):
        email = "testsheep@gmail.com"
        hashed_password = '1729983526'
        response = client.post('/login', {email: email, password: hashed_password})
        self.assertLocationHeader(response,'/welcome')

    def testInvalidEmailValidPassword(self,client):
        pass

    def testValidEmailInvalidPassword(self,client):
        pass

    def testInvalidEmailInvalidPassword(self,client):
        pass
