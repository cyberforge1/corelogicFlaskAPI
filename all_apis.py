from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_restful import Api, Resource
import requests

from current_query import address


# Environmental variables import 
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
api = Api(app)
project_key = os.getenv("SECRET_KEY")

app.secret_key = project_key


api_key = os.environ["api_key"]
client_id = os.environ["client_id"]
client_secret = os.environ["client_secret"]



# FORM TO COLLECT DATA FROM USER
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        unitNumber = request.form.get('unitNumber')
        streetNumber = request.form.get('streetNumber')
        streetName = request.form['streetName']
        streetType = request.form['streetType']
        suburb = request.form['suburb']
        stateCode = request.form['stateCode']
        postCode = request.form['postCode']
        
        if unitNumber is None and streetNumber is None:
            # Handle the case where both unitNumber and streetNumber are missing
            return "Please provide either unitNumber or streetNumber."
        
        address_parts = []
        if unitNumber:
            address_parts.append(unitNumber)
        if streetNumber:
            address_parts.append(streetNumber)
        
        address_parts.extend([streetName, streetType, suburb, stateCode, postCode])
        address = ", ".join(address_parts)
        
        # Redirect to the address-match endpoint passing the address as a URL parameter
        return redirect(f"/address-match?address={address}")
    
    return render_template('index.html')


# Address Match API

class AddressMatch(Resource):
    def get(self):
        # Get the address from the URL parameter
        address = request.args.get('address')
        
        url = 'https://api-uat.corelogic.asia/sandbox/search/au/matcher/address'

        headers = {
            'accept': '*/*',
            'authorization': f'Bearer {api_key}'
        }

        params = {
            'clientName': 'client',
            'q': address
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        try:
            property_id = data['matchDetails']['propertyId']
            # Construct a JSON-serializable dictionary with relevant information
            response_data = {'property_id': property_id, 'status_code': response.status_code}
            return jsonify(response_data)
        except KeyError:
            # KeyError occurred, handle the case and display an alert to the user
            flash("This address is not in the database", "error")
            return 'Address is not in database'
        except Exception as e:
            # Handle other exceptions, and provide a JSON response with the error message
            return 'Address is not in database'



api.add_resource(AddressMatch, "/address-match")




# PROPERTY DETAILS API


class PropertyDetails(Resource):
    def get(self, property_id):  # Get property_id from the URL
        url = f"https://api-uat.corelogic.asia/sandbox/property-details/au/properties/{property_id}/sales"
        headers = {
            'accept': '*/*',
            'authorization': f'Bearer {api_key}'
        }
        
        response = requests.get(url, headers=headers)
        return response.json()

api.add_resource(PropertyDetails, '/property-details/<int:property_id>')  # Modify the route to accept property_id





# PROPERTY TIMELINE API


class PropertyTimeline(Resource):
    def get(self, property_id):  # Get property_id from the URL
        url = f'https://api-uat.corelogic.asia/sandbox/property-timeline/au/properties/{property_id}/timeline'
        headers = {
            'accept': '*/*',
            'authorization': f'Bearer {api_key}'
        }

        response = requests.get(url, headers=headers, params={'withDevelopmentApplications': 'true'})

        return response.json()
    
api.add_resource(PropertyTimeline, "/property-timeline/<int:property_id>")  # Modify the route to accept property_id






# RENTAL VALUATION API


class RentalAvmResource(Resource):
    def get(self, property_id):  # Get property_id from the URL
        url = f'https://api-uat.corelogic.asia/sandbox/property/au/v1/property/{property_id}/rentalAvm.json'
        headers = {
            'Accept': '*/*',
            'Authorization': f'Bearer {api_key}'
        }
        response = requests.get(url, headers=headers)
        return response.json()

api.add_resource(RentalAvmResource, '/rental-avm/<int:property_id>')  # Modify the route to accept property_id





if __name__ == '__main__':
    app.run()
    