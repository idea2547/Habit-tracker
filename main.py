import requests
from requests.api import request
from datetime import datetime

USER = 'sus'
TOKEN = 'fj123402fh8034qefhji'
graph_id = 'graph1'

today = datetime(year=2021, month=10, day = 14)

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token':TOKEN,
    'username':USER,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}



#response =  requests.post(url=pixela_endpoint, json=user_params)

#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

make_pixela = f"{pixela_endpoint}/{USER}/graphs/{graph_id}"
change_pixela = f"{pixela_endpoint}/{USER}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
delete_pixela = f"{pixela_endpoint}/{USER}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)


#create a grpah 

make_pixela_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity":'5',
}

new_pixela_config = {
    "quantity":'2',
}


#response = requests.post(url=make_pixela, json=make_pixela_config, headers=headers)
#response = requests.put(url=change_pixela, json=new_pixela_config, headers=headers)

response = requests.delete(url=delete_pixela, headers=headers)
print(response.text)