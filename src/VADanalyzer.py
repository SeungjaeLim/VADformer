from flask import request
from flask_restx import Resource, Api, Namespace
import random

# Define a Flask-RestX Namespace for the VAD Analyzer API
VAD = Namespace(
    name='VAD',
    description='VAD Analyzer API'
)

# Define an empty list to store the response strings
responses = []

@VAD.route('')
class VADAnalyze(Resource):
    def get(self):  
        # Generate a random VAD score and return it as a dictionary
        response_data = {
            "VAD score": [random.random() for _ in range(3)]
        }
        return response_data

    def post(self):
        # Extract the response string from the request
        response_str = request.data.decode()

        # Append the response string to the list of responses
        responses.append(response_str)

        # Return a message indicating success
        return {'message': f'Response "{response_str}" saved successfully.'}
