from flask import Flask 
from flask_restx import Api, Resource  
from VADanalyzer import VAD

# Create Flask app instance
app = Flask(__name__)  

# Create Flask-RestX API instance
api = Api(
    app,
    version='0.1',  # API version
    title="VAD Analyzer",  # API title
    description="P.EYE XR API Server",  # API description
    terms_url="/",  # URL for API terms and conditions
    contact="seungjaelim@kaist.ac.kr",  # API contact email
    license="MIT"  # API license
)

# Add VAD namespace to the API
api.add_namespace(VAD, '/VAD')

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
