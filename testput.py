import json
import requests

payload = json.dumps({"state": "False"})

headers = {'Content-Type': 'application/json'}

url = "http://localhost:8000/smarthouse/actuator/1/current"

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
