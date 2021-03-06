from flask import Flask
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    application.run(port=8080)