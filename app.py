from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

# import for serverless wsgi
from serverless_wsgi import handle_request

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_current_time():
    current_time = datetime.utcnow().isoformat() + 'Z'
    
    response = {
        "email": "awosanminathaniel0@gmail.com",
        "current_datetime": current_time,
        "github_url": "https://github.com/NathanielWatife/public_api"
    }
    
    return jsonify(response)
def vercel_handler(event, context):
    return handle_request(app, event, context)

if __name__ == '__main__':
    app.run(debug=True)