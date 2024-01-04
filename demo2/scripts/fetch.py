import json
import requests
from demo2.models import UserInfo
#from .models import UserInfo  # Import your model here

# API URL
api_url = 'https://randomuser.me/api/?results=50'  # Replace with the actual API URL

# Fetch data from the API
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    # Assuming data is a list, you can iterate through it and save each item to the database
    for item in data['results']:
        my_model = UserInfo(
            name=item['name']['first'] + ' ' + item['name']['last'],
            street_number=item['address']['street']['number'],
            street_name=item['address']['street']['name'],
            city=item['address']['city'],
            state=item['address']['state'],
            country=item['address']['country'],
            postcode=item['address']['postcode'],
            # Add other fields as needed
        )
        my_model.save()
else:
    print('Failed to fetch data from the API') 
    
    # Delete questions


