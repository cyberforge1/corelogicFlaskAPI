Flask RESTful API - Quakers Hill Property Information
This project is a Flask RESTful API that retrieves property-specific information for the suburb of Quakers Hill, 2763, in Sydney. The API interacts with the CoreLogic sandbox environment to fetch property data.

Setup
To run this API locally, make sure you have Python installed. Additionally, you'll need to set up the necessary environment variables.

Install the required packages:

Copy code
pip install Flask Flask-RESTful requests python-dotenv
Create a .env file in the root directory of the project and set the following environment variables:

makefile
Copy code
SECRET_KEY=<your_secret_key>
api_key=<your_api_key>
client_id=<your_client_id>
client_secret=<your_client_secret>
Ensure you have the current_query.py and quakers_hill_sandboxed_data.json files in the project directory.

Running the API
To run the API, execute the following command in the project directory:

Copy code
python all_apis.py
The API will be available at http://127.0.0.1:5000/.

Endpoints
The API provides the following endpoints:

GET /address-match

This endpoint matches the provided address against the CoreLogic sandbox database and retrieves the property_id.
Parameters:
address: The address to be matched (e.g., /address-match?address=12 Sample St, Quakers Hill, 2763, Sydney).
GET /property-details/<int:property_id>

Retrieves detailed information for the property identified by property_id.
Parameters:
property_id: The property ID obtained from the address-match endpoint.
GET /property-timeline/<int:property_id>

Retrieves the timeline of events for the property identified by property_id.
Parameters:
property_id: The property ID obtained from the address-match endpoint.
GET /rental-avm/<int:property_id>

Retrieves the estimated rental value (AVM) for the property identified by property_id.
Parameters:
property_id: The property ID obtained from the address-match endpoint.
Usage
To retrieve property information, send a GET request to the desired endpoint using a tool like Postman or cURL.

Before making calls to /property-details, /property-timeline, or /rental-avm endpoints, you need to retrieve the property_id from the /address-match route. Follow the steps mentioned in the endpoint documentation to obtain the property_id.

Web Interface
The API also includes a web interface accessible at the root URL (http://127.0.0.1:5000/). The web interface allows you to enter the address details, submit the form, and obtain the property_id by redirecting to the /address-match endpoint. The property_id can then be used to make subsequent calls to other endpoints.

Note
This API can only access data in the CoreLogic sandbox environment, specifically for the location of Quakers Hill with a locality ID: 11770. All sandboxed data is held in the quakers_hill_sandboxed_data.json file.

Feel free to explore the API and retrieve property-specific information for Quakers Hill, 2763, in Sydney!
