import sys
import mysql.connector
from flask_restful import Resource, reqparse
from src.app.models.user import create, list_all


def wrap_email(f):
    def inner(params):
        try:
            print(type(params), file=sys.stderr)
            return f(params)
        except mysql.connector.errors.IntegrityError:
            parser = reqparse.RequestParser()
            parser.add_argument('email')
            args = parser.parse_args()
            return {'message': 'Email already exists', 'data': {"email": args["email"]}}, 422
    return inner


class User(Resource):
    def get(self):
        users = list_all()
        return {'message': 'Success', 'data': {"users": users}}, 200

    @wrap_email
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()

        id = create(args)

        return {'message': 'Created', 'data': {"id": id}}, 201
