import requests
from datetime import datetime, timedelta
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# CREATING A USER IN PIXELA:

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Gaming Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# CREATING A GRAPH IN PIXELA:

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)


add_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = datetime.now()
yesterday = today - timedelta(days=1)

add_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you play today? ")
}

# ADDING A NEW PIXEL TO THE GRAPH:

add_pixel_response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(add_pixel_response.text)

WANTED_DATE = yesterday.strftime("%Y%m%d")

edit_pixel_endpoint = f"{add_pixel_endpoint}/{WANTED_DATE}"

edit_pixel_params = {
    "quantity": "4"
}

# UPDATING THE WANTED PIXEL:

# edit_pixel_response = requests.put(url=edit_pixel_endpoint, json=edit_pixel_params, headers=headers)
# print(edit_pixel_response.text)


DATE_FOR_DELETE = datetime(year=2024, month=12, day=11)
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{DATE_FOR_DELETE.strftime('%Y%m%d')}"

# delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_pixel_response.text)
