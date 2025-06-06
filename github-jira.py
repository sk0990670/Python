# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://solosahej.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF01w2indso--8sbcZI6K9QI-_DTft5bRPNpHqA9tXFqCiOq3tYbXOpB3sEpM70YUvVunAR8apD_oRrpvyAD06bBXz1fdJE4V2La4gYqwF7rmrRQE1NYgUHXqrr1v5QBR16AA2-yGDzE5laTfrke6O3PQbxr7Hy7hDiDabcSHdrxnQ=F5D7C7A7"

    auth = HTTPBasicAuth("sk0990670@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "AB"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
