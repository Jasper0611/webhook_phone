import requests
api_key="urLasOpQ9dxlUucvgcK_hw"
url = "https://api.apollo.io/v1/people/match"

data = {
        "api_key": api_key,
        "first_name": "Marius",
        "last_name": "Dewet",
        "organization_name": "Accrete Consulting",
        "email": "marius@accretesol.com",
        "domain": ".accrete.com",
        "linkedin_url": "https://www.linkedin.com/in/marius-dewet-b5a7695/",
        "reveal_phone_number": True,
        "webhook_url":'http://127.0.0.1:5000/webhook'
        }

headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json'
        }

response = requests.request("POST", url, headers=headers, json=data)
