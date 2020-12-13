import requests
import json
URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={"id":id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

get_data() 

# Create 

def post_data():
    data={
        'name':'Shivang',
        'roll':104,
        'city':'kanpur'
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)


# post_data()

# Update

def update_data():
    data={
        'id':3,
        'name':'Gagan',
        'roll':109,
        'city':'ranchi'
    }
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# update_data()

# Delete

def delete_data():
    data={'id':3}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)


# delete_data()