from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self): # get request when calling this URL
        return {"data": "Hello World!"}
    def post(self): # post request when calling this URL
        return {"data": "Posted!"}

api.add_resource(HelloWorld, "/hello-world")

if __name__ == "__main__":
    app.run(debug=True) # change to False when in production
