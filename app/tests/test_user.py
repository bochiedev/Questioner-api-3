import unittest
import json
from app import create_app

class TestUser(unittest.TestCase):

    def setUp(self):

        """Define test variables and initialize app."""

        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.user_data = {
                            "firstname" : "jacky",
                            "lastname" : "Maribe",
                            "othername" : "jones",
                            "email" : "jackie@gmail.com",
                            "phoneNumber" : "254722123456",
                            "username" : "jackie",
                            "registered" : "1-1-2019",
                            "isAdmin" : "False",
                            "password":"Password2@",
                            "confirm_password":"Password2@"

                            }
        self.invalid_user_data = {
                            "firstname" : "james",
                            "lastname" : "Kabochi",
                            "othername" : "Gakuru",
                            "email" : "bochie@gmail.com",
                            "phoneNumber" : "254722241161",
                            "username" : "bochie",
                            "registered" : "12-2-2019",
                            "isAdmin" : "False",
                            "password":"Password2@",
                            "confirm_password":"confirm_Password2@"
                            }

        self.empty_user_data = {
                            "firstname" : "john",
                            "lastname" : "",
                            "othername" : "james",
                            "email" : "james@gmail.com",
                            "phoneNumber" : "254722241161",
                            "username" : "jimmy",
                            "registered" : "17-1-2019",
                            "isAdmin" : "True",
                            "password":"confirm_Password2@",
                            "confirm_password":"confirm_Password2@"
                            }
        self.wrong_pass_data = {
                            "firstname" : "john",
                            "lastname" : "kiriamiti",
                            "othername" : "james",
                            "email" : "james@gmail.com",
                            "phoneNumber" : "254722241161",
                            "username" : "jimmy",
                            "registered" : "17-1-2019",
                            "isAdmin" : "True",
                            "password":"Confirm2@",
                            "confirm_password":"confirm_Password2@"
                            }
        self.wrong_login_data = {
                            'email' : "email@gmail.com",
                            'password':"Password"

                            }
        self.login_data = {
                            'email' : "email2@gmail.com",
                            'password':"password2"

                            }
        self.invalid_email_data = {
                            'email' : "email2gmail.com",
                            'password':"password2"

                            }
        self.empty_field_data = {
                            'email' : "",
                            'password':"password2"

                            }


    def test_register_user(self):
        """Testing creating a user."""

        response = self.client.post(
            '/api/accounts', data=json.dumps(self.user_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_wrong_password_registration(self):
        """Testing password mismatch verification."""

        response = self.client.post(
            '/api/accounts', data=json.dumps(self.invalid_user_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_empty_field_registration(self):
        """Testing empty field verification."""

        response = self.client.post(
            '/api/accounts', data=json.dumps(self.empty_user_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_empty_field_registration(self):
        """Testing password and confirm password field mismatch verification."""

        response = self.client.post(
            '/api/accounts', data=json.dumps(self.wrong_pass_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_user_login(self):
        """Testing user login."""

        response = self.client.post(
            '/api/login', data=json.dumps(self.login_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_wrong_password_user_login(self):
        """Testing wrong password user login."""

        response = self.client.post(
            '/api/login', data=json.dumps(self.wrong_login_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)

    def test_invalid_email_user_login(self):
        """Testing invalid email address user login."""

        response = self.client.post(
            '/api/login', data=json.dumps(self.invalid_email_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_empty_fields_user_login(self):
        """Testing invalid email address user login."""

        response = self.client.post(
            '/api/login', data=json.dumps(self.empty_field_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_empty_fields_user_login(self):
        """Testing user logout."""

        response = self.client.get('/api/logout')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)




if __name__=='__main__':
    unittest.main()
