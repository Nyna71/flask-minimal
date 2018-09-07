from flask import Flask

application = Flask(__name__)

@application.route("/")
class HelloWorld():
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    application.run(debug=True, port=8080)
