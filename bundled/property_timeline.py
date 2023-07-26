import requests
from flask import Flask, jsonify
from flask_restful import Api, Resource

from current_query import property_id



app = Flask(__name__)
api = Api(app)

# Environmental variables import 
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["api_key"]

class PropertyTimeline(Resource):
    def get(self):
        url = f'https://api-uat.corelogic.asia/sandbox/property-timeline/au/properties/{property_id}/timeline'
        headers = {
            'accept': '*/*',
            'authorization': f'Bearer {api_key}'
        }

        response = requests.get(url, headers=headers, params={'withDevelopmentApplications': 'true'})
        data = response.json()

        return jsonify(data)

api.add_resource(PropertyTimeline, "/property-timeline")

if __name__ == '__main__':
    app.run()
    
    
# useful info: for rent events, for sale events?, sales