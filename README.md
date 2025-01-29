# Public API for HNG Backend Task

A simple Flask API that returns basic user information and the current UTC datetime in ISO 8601 format. Deployed on Vercel.

## API Documentation

### Endpoint
**GET** `https://your-vercel-deployment-url.vercel.app`

### Response Format
```json
{
  "email": "awosanminathaniel0@gmail.com",
  "current_datetime": "2024-05-25T15:30:45Z",
  "github_url": "https://github.com/NathanielWatife/public_api"
}


```
curl https://your-vercel-deployment-url.vercel.app
```




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

Deployment on Vercel
```
Install the Vercel CLI:
```

```
npm install -g vercel
```
Deploy:

vercel --prod
```
Your API will be live at https://your-project-name.vercel.app.
```

Backlinks
Required links to HNG hiring pages:

Here are the required backlinks to HNG's hiring pages:
- [HNG Python Developers](https://hng.tech/hire/python-developers)
- [HNG C# Developers](https://hng.tech/hire/csharp-developers)
- [HNG Golang Developers](https://hng.tech/hire/golang-developers)
- [HNG PHP Developers](https://hng.tech/hire/php-developers)
- [HNG Java Developers](https://hng.tech/hire/java-developers)
- [HNG Node.js Developers](https://hng.tech/hire/nodejs-developers)

Technologies Used
Python 3

Flask (API framework)

Vercel (Serverless deployment)

Flask-CORS (CORS handling)

Note: Replace https://your-vercel-deployment-url.vercel.app with your actual Vercel deployment URL.


### Key Features:
1. **Clear Structure**: Sections for API docs, setup, and backlinks.
2. **Copy-Paste Readiness**: Commands and code snippets can be used directly.
3. **HNG Compliance**: Includes all required backlinks.
4. **Deployment Notes**: Instructions for both local and Vercel hosting.

Let me know if you’d like to tweak any section! 😊