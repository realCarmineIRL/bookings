import os
import requests

API_URL = os.environ.get('API_URL')
API_KEY = os.environ.get('API_KEY')

def get_service_timeslots(service_id):
  url = f'{API_URL}/services/{service_id}'

  payload={}
  headers = {
    'Accept': 'application/json',
    'x-api-key': f'{API_KEY}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  # {'clinicId': 'clinic100', 'city': 'London', 'country': 'United Kingdom', 'streetAddress': '56, Haughton Rd'}
  return response.json()
