from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_current_time():
    current_time = datetime.utcnow().isoformat() + 'Z'
    
    response = {
        "email": "awosanminathaniel0@gmail.com",
        "current_time": current_time,
        "github_url": "https://github.com/NathanielWatife/public_api"
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)