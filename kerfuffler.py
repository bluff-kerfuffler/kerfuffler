from flask import Flask
from flask import jsonify
import requests
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

@app.route('/aimbrain/faceauth', methods=['GET'])
def face_auth(data):
  response = requests.request(
    'POST', 
	'https://api.aimbrain.com:443/v1/face/auth',
	headers={
	  'Content-Type': 'application/json', 
	  'X-aimbrain-apikey': 'test',
	  'X-aimbrain-signature': 'dBxk9M++dNhI7pk+tXvAVaUwlWuOPl8S4wlmrhKhSqs='
	},
	json=data
  )
  return response
  
 #user_id, photo
 
@app.route('/aimbrain/faceenroll', methods=['GET'])
def face_enroll(data):
  response = requests.request(
    'POST', 
	'https://api.aimbrain.com:443/v1/face/enroll',
	headers={
	  'Content-Type': 'application/json', 
	  'X-aimbrain-apikey': 'test',
	  'X-aimbrain-signature': 'VXNfJLbOntEVUlOp6UUwo8D4YyKjNtzspeBCOqZYM9A='
	},
	json=data
  )
  return response
  
@app.route('/aimbrain/sessions', methods=['GET'])
def sessions(data):
  response = requests.request(
    'POST', 
	'https://api.aimbrain.com:443/v1/face/sessions',
	headers={
	  'Content-Type': 'application/json', 
	  'X-aimbrain-apikey': 'test',
	  'X-aimbrain-signature': 'E7vPXCNHsJQhadkTruAbCE+q9fCmRK9Gf+wtl2/3yrA='
	},
	json=data
  )
  return response



@app.route('/')
def index():
  return "hi"
  
if __name__ == '__main__':
    app.run(debug=True)
	
'''
class Aimbrain(Resource)
  def sessions(self, name):
  def face_enrol(self, name):
  def face_auth(self, name);
  def result(self, name):
'''