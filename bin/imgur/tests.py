# import os
# from dotenv import find_dotenv, load_dotenv
import requests

# load_dotenv(find_dotenv())

url = "https://api.imgur.com/oauth2/token"

headers = {
    'Authorization': "Bearer {envBearer}",
    'Cache-Control': "no-cache",
    'Postman-Token': "{token}"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
