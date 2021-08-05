from instabot import *
from flask import Flask, jsonify, request,abort
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource




app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class Scraper(Resource):

    def post(self):
        try:
            data = request.get_json(force=True)
            #print('json_data',data['username'],data['password'],data['targeted_username'])
            username = data['username']
            password = data['password']
            targeted_username = data['targeted_username']
            return get_data(username,password,targeted_username)
        except:
            abort(400, message="Username not Found")

api.add_resource(Scraper, '/api/scraper')


if __name__ == "__main__":
	#app.run(threaded= True,port=5000)
    app.run(debug=True)