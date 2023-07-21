from flask import Flask
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

# Environmental variables import 
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["api_key"]

class PropertyDetails(Resource):
    def get(self):
        url = "https://api-uat.corelogic.asia/sandbox/property-details/au/properties/38873114/sales"
        headers = {
            'accept': '*/*',
            'authorization': f'Bearer {api_key}'
        }
        
        response = requests.get(url, headers=headers)
        return response.json()

api.add_resource(PropertyDetails, '/property-details')


if __name__ == '__main__':
    app.run()