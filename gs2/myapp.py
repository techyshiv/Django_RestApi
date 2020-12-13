import requests
import json
URL="http://127.0.0.1:8000/stucreate/"
data={
    "name":"Shivang",
    "roll":1,
    "city":"Kanpur"
}
json_data=json.dumps(data)
req=requests.post(url=URL,data=json_data)
data=req.json()
print(data)