import flask_unittest
import flask.globals

class TestUser(flast_unittest.ClientTestCase):
    app = Flask(__name__)

    def setUp(self,client):
        pass

    def tearDown(self,client):
        pass

    def testSuccessfulRegister(self,client):
        pass

    def testUnsuccessfulRegister(self,client):
        pass

    def testSuccessfulLogin(self,client):
        pass

    def testInvalidEmailValidPassword(self,client):
        pass

    def testValidEmailInvalidPassword(self,client):
        pass

    def testInvalidEmailInvalidPassword(self,client):
        pass
