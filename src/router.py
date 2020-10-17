from flask_restful import Api
from flask import Flask

# create an instance of Flask
app = Flask(__name__)

# create the API
api = Api(app)


@app.route("/")
def index():
    return 'MakeEat is up and ready for you!!!!'
