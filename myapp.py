# THIS APPLICATION IS FOR TESTING
#IN REAL-WROLD THIS APP MAY BE AN ANDROID APPLICATION, WEB APPLICATION, DESKTOP APPLICATION
# THIS IS NOT A PART OF OUR API
# THIS IS ONLY FOR TESTING PURPOSE
import requests
import json

URL="http://127.0.0.1:8000/studentapi2/"

def get_data(id=None):#getting data from database
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r= requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# get_data() #if here we give id then only those data will appere else all data will appear

def post_data(): #saving this data to database
    data ={
        'name':'jogya',
        'roll':110,
        'city':'Hyderabad',
        }
    #if you getting error 'unsupported media type 'text/plain' in request'
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r= requests.post(url=URL,headers=headers,data=json_data)#pass here : headers=header
    data=r.json()
    print(data)

#post_data()# here we are saving the given data

def update_data():#partial update
    data ={
        'id':5,
        'name':'gutti',
        'city':'ghatkoper',
        }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r= requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# update_data()

def delete_data():#partial update
    data ={
        'id':5,
        }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r= requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

delete_data()