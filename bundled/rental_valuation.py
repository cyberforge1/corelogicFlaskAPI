from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

# Environmental variables import 
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["api_key"]

class RentalAvmResource(Resource):
    def get(self):
        url = 'https://api-uat.corelogic.asia/sandbox/property/au/v1/property/17189053/rentalAvm.json'
        headers = {
            'Accept': '*/*',
            'Authorization': f'Bearer {api_key}'
        }
        response = requests.get(url, headers=headers)
        return response.json()

api.add_resource(RentalAvmResource, '/rental-avm')

if __name__ == '__main__':
    app.run()