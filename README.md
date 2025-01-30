# Public API for HNG Backend Task

A simple Flask API that returns basic user information and the current UTC datetime in ISO 8601 format. Deployed on Vercel.

## API Documentation

### Endpoint
**GET** `https://public-api-teal.vercel.app/`

### Response Format
```json
{
  "email": "awosanminathaniel0@gmail.com",
  "current_datetime": "2024-05-25T15:30:45Z",
  "github_url": "https://github.com/NathanielWatife/public_api"
}

Setup Instructions
Local Development
Clone the repository:

```
git clone https://github.com/NathanielWatife/public_api.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Flask app:

python app.py
Test locally at http://localhost:5000.


```
Your API will be live at https://public-api-teal.vercel.app/.
```

Backlinks
Required links to HNG hiring pages:

Here are the required backlinks to HNG's hiring pages:
- [HNG Python Developers](https://hng.tech/hire/python-developers)

Technologies Used
Python 3

Flask (API framework)

Flask-CORS (CORS handling)