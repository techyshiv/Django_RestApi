import requests
import json
URL="http://127.0.0.1:8000/stuapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={"id":id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

# get_data(2) 

# Create 

def post_data():
    data={
        'name':'Mohit',
        'roll':150,
        'city':'kanpur'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

post_data()

# Update

def update_data():
    data={
        'id':3,
        'name':'Rohit',
        'city':'ranchi'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

# update_data()

# Delete

def delete_data():
    data={'id':3}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)


# delete_data()