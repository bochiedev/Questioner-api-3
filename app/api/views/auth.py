from flask import request
from flask_restplus import Resource


class User(Resource):

    def post(self):
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        othername = data['othername']
        email = data['email']
        phoneNumber = data['phoneNumber']
        username = data['username']
        registered = data['registered']
        isAdmin = data['isAdmin']
        password = data['password']
        confirm_password = data['confirm_password']

        return {'data': firstname}
